<template>
	<div
		class="container mx-auto max-w-lg h-[calc(100vh-80px)] flex row justify-center items-center">
		<div
			class="custom-modal px-16 py-12 rounded-xl shadow-md shadow-slate-400">
			<div class="pb-4 text-h1">Sign in to your account</div>

			<div class="pb-4 relative">
				<label
					for="email"
					class="form-label text-h3"
					>Email</label
				>
				<input
					type="text"
					id="email"
					class="form-control"
					placeholder="id / name / dept / role"
					v-model="search" />
				<div
					v-if="filteredUsers.length"
					name="autocomplete"
					class="absolute max-h-48 max-w-full overflow-y-scroll form-control z-10">
					<div>
						Showing {{ filteredUsers.length }} of
						{{ users.length }} users
					</div>
					<hr class="my-1" />
					<div
						v-for="user of filteredUsers"
						@click="selectUser(user.Email, user.Staff_ID)">
						{{ user.Staff_FName }}&nbsp;{{ user.Staff_LName }} [
						dept: {{ user.Dept }}, rights:
						{{
							user.Role === 1
								? "admin"
								: user.Role === 2
								? "user"
								: user.Role === 3
								? "manager"
								: "HR"
						}}
						]
					</div>
				</div>
				<div
					id="emailValidationHelper"
					class="invalid-feedback">
					Please select a user
				</div>
			</div>
			<div class="pb-4">
				<div class="mb-3">
					<label
						for="basic-url"
						class="form-label text-h3"
						>Password</label
					>
					<input
						type="text"
						disabled
						class="form-control is-valid" />
					<div class="valid-feedback">
						Disabled for mockup purposes
					</div>
				</div>
			</div>

			<div class="">
				<button
					class="btn btn-primary w-full text-btn"
					v-on:click="handleLogin">
					Login
				</button>
			</div>

			<div className="flex justify-center items-center py-4">
				<hr className="grow border-t-2 border-gray-500" />
				<div className="px-3 text-gray-500">or</div>
				<hr className="grow border-t-2 border-gray-500" />
			</div>

			<div class="">
				<button
					class="btn btn-primary w-full text-sm fw-bold"
					v-on:click="handleSSO">
					Sign in with single sign-on (SSO)
				</button>
			</div>
			<div
				v-if="showSSOError"
				class="absolute bottom-3 right-5 z-10">
				<div
					class="alert alert-warning fade show"
					role="alert">
					<h4 class="alert-heading">Oh no!</h4>
					SSO will only be implemented in future sprints.
				</div>
			</div>
		</div>
	</div>
</template>
<script>
import { ref } from "vue";

export default {
	data() {
		return {
			users: [],
			showSSOError: false,
			reload: true,
			search: "",
			filteredUsers: [],
			selectedUserId: 0,
		};
	},
	created() {},

	mounted() {
		//console.log(this.$store.state.user);
		this.fetchUsers();
		console.log(this.users);
	},
	computed: {
		filteredUsers() {
			if (this.search === "") return [];
			if (this.search.includes("@")) return [];
			const searchLower = this.search.toLowerCase();
			return this.users.filter((user) => {
				const roleMap = { admin: 1, user: 2, manager: 3, hr: 4 };
				for (let role of Object.keys(roleMap)) {
					if (role.includes(searchLower)) {
						var userRole = roleMap[role];
					}
				}
				if (
					user.Staff_ID.toString().includes(searchLower) ||
					user.Staff_FName.toLowerCase().includes(searchLower) ||
					user.Staff_LName.toLowerCase().includes(searchLower) ||
					(
						user.Staff_FName.toLowerCase() +
						" " +
						user.Staff_LName.toLowerCase()
					).includes(searchLower) ||
					user.Dept.toLowerCase().includes(searchLower) ||
					user.Role === userRole
				) {
					return user;
				}
			});
		},
	},
	methods: {
		async fetchUsers() {
			try {
				const apiUrl = "http://localhost:5000/api/users";
				const response = await fetch(apiUrl, { mode: "cors" });
				const data = await response.json();
				this.users = data.users;
				console.log(this.users);
			} catch (error) {
				console.error(
					"There was a problem with the fetch operation:",
					error
				);
			}
		},
		selectUser(email, id) {
			this.search = email;
			this.selectedUserId = id;
			this.filteredUsers = [];
		},
		async handleLogin() {
			document.getElementById("email").classList.remove("is-invalid");
			document
				.getElementById("emailValidationHelper")
				.classList.remove("block");
			if (this.search === "") {
				document.getElementById("email").classList.add("is-invalid");
				document
					.getElementById("emailValidationHelper")
					.classList.add("block");
				return;
			}
			try {
				const apiUrl = `http://localhost:5000/api/userID?id=${encodeURIComponent(
					this.selectedUserId
				)}`;
				const response = await fetch(apiUrl);
				const data = await response.json();
				console.log(data);
				const user = data;
				this.$store.commit("setUser", {
					id: user.Staff_ID,
					fName: user.Staff_FName,
					lName: user.Staff_LName,
					dept: user.Dept,
					country: user.country,
					email: user.Email,
					role: user.Role,
				});
				this.$router.push({ name: "Home" });
			} catch (error) {
				console.error(error);
			}
		},
		handleSSO() {
			this.showSSOError = true;
			setTimeout(() => {
				this.showSSOError = false;
			}, 5000);
		},
	},
};
</script>
