<template>
	<!-- Mobile -->
	<nav
		class="flex md:hidden navbar z-10 px-4 bg-navbar/[0.85] navbar-dark h-16 w-full border-0 border-solid border-b border-primary backdrop-blur-[3px]">
		<div class="flex flex-row justify-between w-full">
			<button
				class="navbar-toggler border-none p-0"
				type="button"
				data-bs-toggle="offcanvas"
				data-bs-target="#menu"
				aria-controls="menu"
				aria-expanded="false"
				aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div
				class="offcanvas offcanvas-start h-screen w-64 bg-navbar"
				id="menu">
				<div class="px-4 h-full">
					<button
						class="navbar-toggler border-none px-0 py-4"
						type="button"
						data-bs-toggle="offcanvas"
						data-bs-target="#menu"
						aria-controls="menu"
						aria-expanded="false"
						aria-label="Toggle navigation">
						<span class="navbar-toggler-icon"></span>
					</button>
					<!-- Side NavBar content -->
					<div
						class="flex flex-col gap-2 text-white h-[calc(100vh-64px)] justify-between pb-4">
						<div>
							<div class="">
								<div
									v-if="true"
									class="cursor-pointer p-2"
									@click="handleHome()"
									data-bs-toggle="offcanvas"
									data-bs-target="#menu">
									Home
								</div>

								<div
									class="cursor-pointer p-2 mt-2"
									@click="handleProfile">
									View Profile
								</div>
							</div>
						</div>
						<div
							class="rounded-xl border-2 border-solid border-primary p-4">
							<div class="">
								{{ user.fName }} {{ user.lName }},&nbsp;
								{{ user.dept }}
							</div>
							<div
								class="btn btn-primary mt-4"
								@click="handleLogout">
								Log out
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- Logo -->
			<div
				class="logo flex items-center cursor-pointer"
				@click="handleHome()">
				<img
					src="/portal.png"
					width="40"
					height="40" />
			</div>
		</div>
	</nav>
	<!-- Web -->
	<div
		class="hidden md:flex navbar z-10 px-4 bg-navbar/[0.85] text-white h-16 w-full border-0 border-solid border-b border-primary backdrop-blur-[3px]">
		<div
			class="logo flex items-center cursor-pointer"
			@click="handleHome()">
			<img
				src="/portal.png"
				width="40"
				height="40" />
			<div class="ml-3 text-h1">Skill Based Role Portal</div>
		</div>
		<div class="flex">
			<!-- Links -->
			<!-- <div class="flex items-center justify-between pr-8"> -->
			<!-- Admin -->
			<!-- <a v-if="user.accessRights == 0">admin link</a> -->
			<!-- Staff -->
			<!-- <a v-if="user.accessRights == 1">staff link</a> -->
			<!-- Manager -->
			<!-- <a v-if="user.accessRights == 2">manager link</a> -->
			<!-- </div> -->
			<!-- Dev panel -->
			<div
				@mouseover="showDevPanel = true"
				@mouseleave="showDevPanel = false"
				class="pr-8 flex items-center">
				Dev
				<div
					v-if="showDevPanel"
					class="absolute right-10 bg-zinc-600 p-4 rounded-lg top-10">
					<span class="text-h3 text-lg">User details:</span><br />
					accessRights:
					{{
						user.role == 1
							? "admin"
							: user.role == 2
							? "user"
							: user.role == 3
							? "manager"
							: user.role == 4
							? "HR"
							: "error"
					}}<br />
					userID: {{ user.id }}<br />
					email: {{ user.email }}<br />
					fName: {{ user.fName }}<br />
					lName: {{ user.lName }}<br />
					dept: {{ user.dept }}<br />
				</div>
			</div>
			<!-- Profile -->
			<div
				class="user"
				type="button"
				data-bs-toggle="dropdown">
				<div
					class="w-10 h-10 bg-avatar rounded-full flex justify-center items-center">
					<span class="initials text-dark text-initials">
						{{ user.fName.slice(0, 1)
						}}<span class="pr-[1px]"></span
						>{{ user.lName.slice(0, 1) }}
					</span>
				</div>
			</div>
			<ul class="dropdown-menu dropdown-menu-end">
				<li>
					<a
						class="dropdown-item"
						@click="handleProfile"
						>Profile</a
					>
				</li>
				<li>
					<a
						class="dropdown-item"
						@click="handleLogout"
						>Log out</a
					>
				</li>
			</ul>
		</div>
	</div>
</template>
<script>
export default {
	data() {
		return {
			user: this.$store.state.user,
			showDevPanel: false,
		};
	},
	created() {},
	mounted() {
		console.log(this.user);
	},
	methods: {
		handleLogout() {
			sessionStorage.clear();
			window.location.href = "/";
			//this.$router.push({ name: "Login" })
		},
		handleHome() {
			this.$router.push({ name: "Home" });
		},
		handleProfile() {
			console.log("not yet implemented");
		},
	},
};
</script>
