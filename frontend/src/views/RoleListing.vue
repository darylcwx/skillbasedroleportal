<template>
	<div class="container mx-auto max-w-2xl min-h-[calc(100vh-80px)] pt-16">
		<!-- Role details -->
		<div class="pt-8">
			<div
				class="custom-modal p-6 rounded-xl shadow-lg shadow-gray-700"
				:class="isExpired() ? 'custom-modal-expired' : ''">
				<div class="flex justify-between items-center">
					<div class="flex items-center">
						<div class="text-h1 mr-2">{{ name }}</div>
						<component
							:is="icons[role.roleName]"
							class="h-6 w-6" />
					</div>
					<div class="">
						Ends: <b>{{ role.deadline }}</b>
					</div>
				</div>
				<div class="mt-4">{{ role.description }}</div>
				<div class="flex justify-between items-center mt-4">
					<div
						v-if="isExpired()"
						class="text-danger text-btn">
						This listing has expired.
					</div>
					<div></div>
					<div class="flex gap-2">
						<button
							v-if="user.role == 1 || user.role == 4"
							class="btn btn-primary text-btn"
							:class="isExpired() ? 'disabled' : ''"
							data-bs-toggle="modal"
							data-bs-target="#editModal">
							Edit
						</button>

						<!-- Open confirm modal -->
						<button
							type="button"
							class="btn btn-primary text-btn"
							:class="isExpired() ? 'disabled' : ''"
							data-bs-toggle="modal"
							data-bs-target="#confirmApplyModal">
							Apply
						</button>
					</div>
				</div>
			</div>
		</div>
		<div class="absolute top-1/2">
			<ModalConfirmation
				id="confirmApplyModal"
				@confirmed="handleConfirm" />
			<svgSuccess
				v-if="this.success"
				:message="this.message" />
			<svgError
				v-if="this.error"
				:message="this.message" />
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
						v-else-if="
							this.roleSkillMatch['Staff Matched Skills']
								.length == 0 &&
							this.roleSkillMatch['Staff Missing Skills']
								.length == 0
						">
						My percentage match: <b>N/A</b>
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
					<div
						v-if="
							!this.roleSkillMatchNotLoaded &&
							this.roleSkillMatch['Staff Matched Skills']
								.length == 0 &&
							this.roleSkillMatch['Staff Missing Skills']
								.length == 0
						">
						No skills required.
					</div>
					<span
						v-for="skillsMatched in roleSkillMatch[
							'Staff Matched Skills'
						]"
						class="badge custom-pill bg-success mt-3 mr-3"
						>{{ skillsMatched }}
					</span>
					<span
						v-for="skillsMismatched in roleSkillMatch[
							'Staff Missing Skills'
						]"
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
					v-if="
						!this.applicantsNotLoaded && this.applicants.length == 0
					"
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
import { iconsObject } from "../utils/icons.js";
import { SquaresPlusIcon, QueueListIcon } from "@heroicons/vue/24/solid";
import ModalEditRoleListing from "../components/ModalEditRoleListing.vue";
import ModalConfirmation from "../components/ModalConfirmation.vue";
import svgSuccess from "../components/svgSuccess.vue";
import svgError from "../components/svgError.vue";
import { globalVars } from "../utils/globalVars.js";
export default {
	props: ["name"],
	components: {
		Application,
		SquaresPlusIcon,
		QueueListIcon,
		ModalEditRoleListing,
		ModalConfirmation,
		svgSuccess,
		svgError,
	},
	data() {
		return {
			user: this.$store.state.user,
			role: this.$store.state.role,
			roleSkillMatch: this.$store.state.roleskillmatch,
			roleSkillMatchNotLoaded: false,
			applicants: [], // [{}, {}, {}]
			applicantsNotLoaded: true,
			success: false,
			error: false,
			icons: iconsObject,
		};
	},

	created() {},

	mounted() {
		// this.fetchRoleSkillMatch();
		this.fetchAllApplicants();
	},

	methods: {
		// async fetchRoleSkillMatch() {
		// 	try {
		// 		const apiURL = `http://localhost:5000/api/roleskillmatch?sid=${encodeURIComponent(
		// 			this.user.id
		// 		)}&rolename=${encodeURIComponent(this.name)}`;
		// 		const response = await fetch(apiURL, { mode: "cors" });
		// 		let roleSkillMatchObject = await response.json();
		// 		roleSkillMatchObject["Percentage Match"] = parseInt(
		// 			roleSkillMatchObject["Percentage Match"]
		// 		);
		// 		this.roleSkillMatch = roleSkillMatchObject;
		// 		this.roleSkillMatchNotLoaded = false;
		// 	} catch (error) {
		// 		console.error(error);
		// 	}
		// },

		async fetchAllApplicants() {
			try {
				const apiURL = `http://localhost:5000/api/allroleskillmatch?lid=${encodeURIComponent(
					this.role.listingID
				)}`;
				const response = await fetch(apiURL, { mode: "cors" });
				let applicantObject = await response.json();
				for (let i in applicantObject["Applicants"]) {
					applicantObject["Applicants"][i]["Percentage Match"] =
						parseInt(
							applicantObject["Applicants"][i]["Percentage Match"]
						);
				}
				this.applicants = applicantObject["Applicants"];
				this.applicantsNotLoaded = false;
			} catch (error) {
				console.error(error);
			}
		},
		async handleConfirm() {
			// use these values
			// console.log(this.user.id);
			// console.log(this.role.listingID);

			let result = await this.handleApply();
			let status = result.status;
			let displayMessage = result.displayMessage;

			if (status == "success") {
				this.success = true;
				this.message = displayMessage;
				setTimeout(() => {
					this.success = false;
					location.reload();
				}, globalVars.svgTimeout);
			} else {
				this.error = true;
				this.message = displayMessage;
				setTimeout(() => {
					this.error = false;
				}, globalVars.svgTimeout);
			}
		},
		async handleApply() {
			// refetch all applicants for updated data
			await this.fetchAllApplicants();
			// check if current date is before deadline
			let currentDate = new Date();
			let deadline = new Date(this.role.deadline);

			// check if current date is before deadline
			if (currentDate > deadline) {
				return {
					status: "error",
					displayMessage: "Current date is after deadline.",
				};
			}

			//check for duplicate application
			for (let applicant of this.applicants) {
				if (applicant["Staff ID"] == this.user.id) {
					return {
						status: "error",
						displayMessage:
							"You have already applied for this role!",
					};
				}
			}

			// insert into staff_application table the application
			try {
				const apiURL = `http://localhost:5000/api/updateStaffApplication/${encodeURIComponent(
					this.role.listingID
				)}/${encodeURIComponent(this.user.id)}`;
				const response = await fetch(apiURL, {
					mode: "cors",
					method: "POST",
				});
				let data = await response.json();
				if (data["Status"] == "Data updated successfully.") {
					return {
						status: "success",
						displayMessage: "Successfully Applied",
					};
				} else {
					return {
						status: "error",
						displayMessage: data["Status"],
					};
				}
			} catch (error) {
				console.error(error);
			}
		},
		isExpired() {
			const today = new Date();
			const roleDate = new Date(this.role.deadline);
			roleDate.setDate(roleDate.getDate() + 1);
			return today >= roleDate;
		},
	},
};
</script>
