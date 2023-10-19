<template>
	<div class="pt-8">
		<div
			class="p-6 custom-modal rounded-xl text-dark"
			:class="
				isExpired()
					? 'custom-modal-expired'
					: 'hover:scale-105 transition duration-200 ease-in-out hover:shadow-lg hover:shadow-gray-500'
			">
			<div class="flex justify-between items-center">
				<div class="flex items-center">
					<div class="text-h1 mr-2">{{ name }}</div>
					<component
						:is="icons[this.name]"
						class="h-6 w-6" />
				</div>
				<div class="">
					Ends: <b>{{ deadline }}</b>
				</div>
			</div>
			<div class="mt-4">{{ desc }}</div>
			<div class="flex justify-between items-center mt-4">
				<div
					v-if="isExpired()"
					class="text-danger text-btn">
					This listing has expired.
				</div>
				<div></div>
				<button
					class="btn btn-primary text-btn"
					@click="handleClick">
					See more
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import {
	ComputerDesktopIcon,
	CommandLineIcon,
	UserGroupIcon,
	UsersIcon,
} from "@heroicons/vue/24/solid";
export default {
	props: ["role"],
	data() {
		return {
			user: this.$store.state.user,
			name: this.role.Role_Name,
			desc: this.role.Description,
			deadline: this.role.Deadline,
			icons: {
				Clerk: ComputerDesktopIcon,
				"IT Support": CommandLineIcon,
				"Human Resource": UserGroupIcon,
				Manager: UsersIcon,
			},
		};
	},
	created() {},
	mounted() {
		// console.log(new Date(this.deadline));
		// console.log(new Date());
		// console.log(new Date(this.deadline) >= new Date());
	},
	methods: {
		handleClick() {
			this.$store.commit("setRole", {
				listingID: this.role.Listing_ID,
				roleName: this.name,
				description: this.desc,
				deadline: this.deadline,
				icons: this.icons,
			});

			this.$router.push({ name: "Role", params: { name: this.name } });
		},
		isExpired() {
			const today = new Date();
			const roleDate = new Date(this.deadline);
			roleDate.setDate(roleDate.getDate() + 1);
			console.log(this.role.Role_Name, today >= roleDate);
			return today >= roleDate;
		},
	},
};
</script>
