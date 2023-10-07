<template>
	<div
		class="modal fade"
		id="editModal"
		tabindex="-1"
		aria-labelledby="editModalLabel"
		aria-hidden="true">
		<div class="modal-dialog modal-md h-[calc(100vh-56px)] flex items-center">
			<div class="modal-content">
				<div class="modal-header border-0 p-4">
					<div
						class="modal-title text-h2"
						id="editModalLabel">
						Edit Role Listing
					</div>
					<button
						type="button"
						class="btn-close"
						data-bs-dismiss="modal"
						aria-label="Close"></button>
				</div>
				<div class="modal-body p-4">
					<!-- Edit -->
					<form class="flex flex-wrap md:justify-between">
						<div class="w-full md:w-auto flex-col mb-6">
							<label
								for="roleName"
								class="form-label text-h3"
								>Role Name</label
							>
							<input
								id="roleName"
								type="text"
								class="form-control"
								v-model="this.roleName"
								disabled
								readonly />
						</div>
						<div class="w-full md:w-auto flex-col mb-6">
							<label
								for="roleDeadline"
								class="form-label text-h3"
								>Deadline</label
							>
							<div class="text-bold">
								<VueDatePicker
									id="roleDeadline"
									v-model="this.roleDeadline"
									:format="format"
									:min-date="new Date()"
									:enable-time-picker="false"
									auto-apply>
								</VueDatePicker>
							</div>
						</div>
					</form>
					<div class="">
						<label
							for="roleDescription"
							class="form-label text-h3">
							Role Description
						</label>
						<textarea
							id="roleDescription"
							class="form-control"
							v-model="this.roleDescription"></textarea>
					</div>
				</div>
				<div class="modal-footer border-0">
					<button
						type="button"
						class="btn btn-secondary text-btn"
						data-bs-dismiss="modal">
						Cancel
					</button>
					<!-- Open confirm modal -->
					<button
						type="button"
						class="btn btn-primary text-btn"
						data-bs-toggle="modal"
						data-bs-target="#confirmEditModal">
						Save changes
					</button>
				</div>
			</div>
		</div>
	</div>
	<div class="absolute top-1/2">
		<ModalConfirmation
			id="confirmEditModal"
			@confirmed="handleConfirm" />
	</div>
	<svgSuccess
		v-if="this.success"
		:message="this.message" />
	<svgError
		v-if="this.error"
		:message="this.message" />
</template>

<script>
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import ModalConfirmation from "../components/ModalConfirmation.vue";
import svgSuccess from "../components/svgSuccess.vue";
import svgError from "../components/svgError.vue";
export default {
	components: { VueDatePicker, ModalConfirmation, svgSuccess, svgError },
	props: ["role"],
	data() {
		return {
			roleName: this.role.roleName,
			roleDescription: this.role.description,
			roleDeadline: this.role.deadline,
			success: false,
			error: false,
			message: "",
		};
	},
	mounted() {
		console.log(this.role);
	},
	methods: {
		format(date) {
			if (!date) return "";
			const formatted = date.toLocaleString("en-US", {
				year: "numeric",
				month: "long",
				day: "numeric",
			});
			return formatted;
		},
		handleConfirm() {
			this.message = "";
			console.log("second modal called and 'Confirm' clicked");

			// use these values
			console.log(this.roleName);
			console.log(this.roleDescription);
			console.log(this.roleDeadline);

			let answer = this.updateRole();
			answer = "success";

			// error handling
			if (answer == "success") {
				this.success = true;
				this.message = "Successfully updated role listing!";

				setTimeout(() => {
					this.success = false;
				}, 3000);
				// might need to force rerender here once data updated
			} else {
				this.error = true;
				this.message = response.error;

				setTimeout(() => {
					this.error = false;
				}, 3000);
				//3000
			}
		},
		async updateRole() {
			try {
				const apiURL = `http://localhost:5000/api/`;
				const response = await fetch(apiURL, { mode: "cors" });
				let data = await response.json();
			} catch (error) {
				console.error(error);
			}
		},
	},
};
</script>

<style lang="scss">
:root {
	/*General*/
	--dp-font-family: "Open Sans", roboto, -apple-system, blinkmacsystemfont,
		"Segoe UI", oxygen, ubuntu, cantarell, "Helvetica Neue", sans-serif;
	--dp-border-radius: 4px; /*Configurable border-radius*/
	--dp-cell-border-radius: 999px; /*Specific border radius for the calendar cell*/
	--dp-common-transition: all 0.1s ease-in; /*Generic transition applied on buttons and calendar cells*/

	/*Sizing*/
	--dp-button-height: 35px; /*Size for buttons in overlays*/
	--dp-month-year-row-height: 35px; /*Height of the month-year select row*/
	--dp-month-year-row-button-size: 35px; /*Specific height for the next/previous buttons*/
	--dp-button-icon-height: 25px; /*Icon sizing in buttons*/
	--dp-cell-size: 35px; /*Width and height of calendar cell*/
	--dp-cell-padding: 5px; /*Padding in the cell*/
	--dp-common-padding: 10px; /*Common padding used*/
	--dp-input-icon-padding: 35px; /*Padding on the left side of the input if icon is present*/
	--dp-input-padding: 6px 30px 6px 12px; /*Padding in the input*/
	--dp-menu-min-width: 320px; /*Adjust the min width of the menu*/
	--dp-action-buttons-padding: 2px 5px; /*Adjust padding for the action buttons in action row*/
	--dp-row-margin: 8px 0; /*Adjust the spacing between rows in the calendar*/
	--dp-calendar-header-cell-padding: 0.5rem; /*Adjust padding in calendar header cells*/
	--dp-two-calendars-spacing: 10px; /*Space between multiple calendars*/
	--dp-overlay-col-padding: 3px; /*Padding in the overlay column*/
	--dp-time-inc-dec-button-size: 32px; /*Sizing for arrow buttons in the time picker*/
	--dp-menu-padding: 6px 8px; /*Menu padding*/

	/*Font sizes*/
	--dp-font-size: 1rem; /*Default font-size*/
	--dp-preview-font-size: 0.8rem; /*Font size of the date preview in the action row*/
	--dp-time-font-size: 0.8rem; /*Font size in the time picker*/

	/*Transitions*/
	--dp-animation-duration: 0.1s; /*Transition duration*/
	--dp-menu-appear-transition-timing: cubic-bezier(
		0.4,
		0,
		1,
		1
	); /*Timing on menu appear animation*/
	--dp-transition-timing: ease-out; /*Timing on slide animations*/
}
</style>
