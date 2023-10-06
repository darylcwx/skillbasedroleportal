<template>
	<div class="container mx-auto max-w-2xl min-h-[calc(100vh-56px)] mt-14">
		<!-- Role details -->
		<div class="pt-8">
			<div class="custom-modal p-6 rounded-xl shadow-lg shadow-gray-700">
				<div class="flex justify-between items-center">
					<div class="flex items-center">
						<div class="text-h1 mr-2">{{ name }}</div>
						<component
							:is="this.icons[name]"
							class="h-6 w-6" />
					</div>
					<div class="">
						Ends: <b>{{ role.deadline }}</b>
					</div>
				</div>
				<div class="mt-4">{{ role.description }}</div>
				<div class="flex justify-end gap-2 mt-4">
					<button
						v-if="user.accessRights == 0"
						class="btn btn-primary text-btn"
						@click="handleEdit"
						data-bs-toggle="modal"
						data-bs-target="#editModal">
						Edit
					</button>
					<button
						class="btn btn-primary text-btn"
						@click="handleClick">
						Apply
					</button>
				</div>
			</div>
		</div>

		<!-- Skills Required -->
		<div class="pt-8">
			<div class="custom-modal p-6 rounded-xl shadow-lg shadow-gray-700">
				<div class="flex items-center justify-between">
					<div class="flex items-center">
						<div class="text-h1 mr-2">Skills Required</div>
						<SquaresPlusIcon class="h-6 w-6" />
					</div>
					<div
						v-if="Object.keys(roleSkillMatch).length == 0"
						class="">
						My percentage match: <b>... %</b>
					</div>
					<div
						v-else
						class="">
						My percentage match:
						<b>{{ roleSkillMatch["Percentage Match"] }}%</b>
					</div>
				</div>
				<div
					name="matched"
					class="mt-4 flex-col">
					<div
						v-if="this.roleSkillMatchNotLoaded"
						class="placeholder-wave">
						<span
							class="placeholder col-3 badge custom-pill-no-shadow bg-placeholder text-placeholder mt-3 mr-3">
							placeholder
						</span>
						<span
							class="placeholder col-5 badge custom-pill-no-shadow bg-placeholder text-placeholder mt-3 mr-3">
							placeholder
						</span>
						<span
							class="placeholder col-4 badge custom-pill-no-shadow bg-placeholder text-placeholder mt-3 mr-3">
							placeholder
						</span>
						<span
							class="placeholder col-2 badge custom-pill-no-shadow bg-placeholder text-placeholder mt-3 mr-3">
							placeholder
						</span>
						<span
							class="placeholder col-9 badge custom-pill-no-shadow bg-placeholder text-placeholder mt-3 mr-3">
							placeholder
						</span>
					</div>
					<span
						v-for="skillsMatched in roleSkillMatch['Staff Matched Skills']"
						class="badge custom-pill bg-success mt-3 mr-3"
						>{{ skillsMatched }}
					</span>
					<span
						v-for="skillsMismatched in roleSkillMatch['Staff Missing Skills']"
						class="badge custom-pill bg-secondary mt-3 mr-3"
						>{{ skillsMismatched }}
					</span>
				</div>
			</div>
		</div>

		<!-- Applicants -->
		<div class="pt-8 pb-8">
			<!-- need to change the v-if -->
			<div
				v-if="user.dept == 'HR'"
				class="custom-modal p-6 rounded-xl shadow-lg shadow-gray-700">
				<div class="flex items-center">
					<div class="text-h1 mr-2">Applicants</div>
					<QueueListIcon class="h-6 w-6" />
				</div>
				<div
					v-if="this.applicantsNotLoaded"
					class="placeholder-wave">
					<span
						class="placeholder bg-placeholder text-placeholder rounded-xl mt-4 h-72 w-full select-none">
						placeholder
					</span>
				</div>
				<div
					v-if="!this.applicantsNotLoaded && this.applicants.length == 0"
					class="">
					<div class="mt-4">No applicants found.</div>
				</div>
				<div
					v-else
					class="overflow-auto h-112">
					<div v-for="applicant of this.applicants">
						<Application :application="applicant" />
					</div>
				</div>
			</div>
		</div>

		<!-- Edit Role Listing -->
		<ModalEditRoleListing :role="this.role" />
	</div>
</template>

<script>
import Application from "../components/Application.vue";
import {
	ComputerDesktopIcon,
	CommandLineIcon,
	UserGroupIcon,
	UsersIcon,
} from "@heroicons/vue/24/solid";
import { SquaresPlusIcon, QueueListIcon } from "@heroicons/vue/24/solid";
import ModalEditRoleListing from "../components/ModalEditRoleListing.vue";
import ModalConfirmation from "../components/ModalConfirmation.vue";
export default {
	props: ["name"],
	components: {
		Application,
		SquaresPlusIcon,
		QueueListIcon,
		ModalEditRoleListing,
		ModalConfirmation,
	},
	data() {
		return {
			user: this.$store.state.user,
			role: this.$store.state.role,
			icons: {
				Clerk: ComputerDesktopIcon,
				"IT Support": CommandLineIcon,
				"Human Resource": UserGroupIcon,
				Manager: UsersIcon,
			},
			roleSkillMatch: {},
			roleSkillMatchNotLoaded: true,
			applicants: [],
			applicantsNotLoaded: true,
			showEditModal: false,
		};
	},

	created() {},

	mounted() {
		this.fetchRoleSkillMatch();
		this.fetchAllApplicants();
		console.log(this.applicants);
	},

	methods: {
		async fetchRoleSkillMatch() {
			try {
				const apiURL = `http://localhost:5000/api/roleskillmatch?sid=${encodeURIComponent(
					this.user.id
				)}&rolename=${encodeURIComponent(this.name)}`;
				const response = await fetch(apiURL, { mode: "cors" });
				let roleSkillMatchObject = await response.json();
				roleSkillMatchObject["Percentage Match"] = parseInt(
					roleSkillMatchObject["Percentage Match"]
				);
				this.roleSkillMatch = roleSkillMatchObject;
				this.roleSkillMatchNotLoaded = false;
			} catch (error) {
				console.error(error);
			}
		},

		async fetchAllApplicants() {
			try {
				const apiURL = `http://localhost:5000/api/allroleskillmatch?lid=${encodeURIComponent(
					this.role.listingID
				)}`;
				const response = await fetch(apiURL, { mode: "cors" });
				let applicantObject = await response.json();
				for (let i in applicantObject["Applicants"]) {
					applicantObject["Applicants"][i]["Percentage Match"] = parseInt(
						applicantObject["Applicants"][i]["Percentage Match"]
					);
				}
				this.applicants = applicantObject["Applicants"];
				this.applicantsNotLoaded = false;
			} catch (error) {
				console.error(error);
			}
		},

		handleEdit() {
			this.showEditModal = true;
		},
		handleApply() {},
	},
};
</script>
