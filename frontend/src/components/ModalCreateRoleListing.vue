<template>
	<div
		class="modal fade"
		id="createModal"
		tabindex="-1"
		aria-labelledby="createModalLabel"
		aria-hidden="true">
		<div
			class="modal-dialog modal-md h-[calc(100vh-56px)] flex items-center">
			<div class="modal-content">
				<div class="modal-header border-0 p-4">
					<div
						class="modal-title text-h2"
						id="createModalLabel">
						Create Role Listing
					</div>
					<button
						type="button"
						class="btn-close"
						data-bs-dismiss="modal"
						aria-label="Close"></button>
				</div>
				<div class="modal-body p-4">
					<form
						class="flex flex-wrap md:justify-between needs-validation"
						novalidate>
						<div class="w-full md:w-auto flex-col mb-6">
							<label
								for="roleName"
								class="form-label text-h3"
								>Role Name</label
							>
							<select
								id="roleName"
								v-model="this.roleName"
								@change="this.populateDesc()"
								class="w-full form-select"
								required>
								<option selected>Select a role</option>
								<option v-for="role of this.roles">
									{{ role.Role_Name }}
								</option>
							</select>
							<div
								id="roleNameValidationHelper"
								class="invalid-feedback">
								Role name cannot be empty.
							</div>
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
							v-model="this.roleDescription"
							rows="10"
							required>
						</textarea>
						<div
							id="roleDescriptionValidationHelper"
							class="invalid-feedback">
							Role description cannot be empty.
						</div>
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
						@click="handleSave">
						Save Changes
					</button>
				</div>
			</div>
		</div>
	</div>
	<ModalConfirmation
		id="confirmModal"
		@confirmed="handleConfirm" />
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
import { globalVars } from "../utils/globalVars.js";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle.js";
export default {
	components: { VueDatePicker, ModalConfirmation, svgSuccess, svgError },
	setup() {},
	data() {
		return {
			roleName: "Select a role",
			roleDescription: "",
			roleDeadline: new Date(),
			roles: {},
			success: false,
			error: false,
			message: "",
			errorFlag: false,
		};
	},
	mounted() {
		// Get roles for roleName DDL
		this.getRoles();

		// Removes any validation
		const roleName = document.getElementById("roleName");
		const roleNameValidationHelper = document.getElementById(
			"roleNameValidationHelper"
		);
		roleName.classList.remove("is-invalid");
		roleNameValidationHelper.classList.remove("was-validated");

		const roleDescription = document.getElementById("roleDescription");
		const roleDescriptionValidationHelper = document.getElementById(
			"roleDescriptionValidationHelper"
		);
		roleDescription.classList.remove("is-invalid");
		roleDescriptionValidationHelper.classList.remove("was-validated");
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
		populateDesc() {
			// console.log(this.roles)
			for (let i = 0; i < this.roles.length; i++) {
				// console.log(this.roles[i].Role_Name);
				if (this.roles[i].Role_Name == this.roleName) {
					this.roleDescription = this.roles[i].Role_Desc;
				}
			}
			return;
		},
		async getRoles() {
			const apiURL = `http://localhost:5000/api/roles`;
			const response = await fetch(apiURL, { mode: "cors" });
			let data = await response.json();
			this.roles = data["roles"];
			return;
		},
		handleSave() {
			// Reset error variables and flag
			this.errorFlag = false;
			const roleName = document.getElementById("roleName");
			const roleNameValidationHelper = document.getElementById(
				"roleNameValidationHelper"
			);
			const roleDescription = document.getElementById("roleDescription");
			const roleDescriptionValidationHelper = document.getElementById(
				"roleDescriptionValidationHelper"
			);
			roleName.classList.remove("is-invalid");
			roleNameValidationHelper.classList.remove("was-validated");
			roleDescription.classList.remove("is-invalid");
			roleDescriptionValidationHelper.classList.remove("was-validated");

			// Validation
			if (this.roleName == "Select a role") {
				roleName.classList.add("is-invalid");
				roleNameValidationHelper.classList.add("was-validated");
				roleDescription.classList.add("is-invalid");
				roleDescriptionValidationHelper.classList.add("was-validated");
				return;
			}
			if (this.roleName && this.roleDescription == "") {
				roleDescription.classList.add("is-invalid");
				roleDescriptionValidationHelper.classList.add("was-validated");
				return;
			}

			const createModal = bootstrap.Modal.getInstance("#createModal");
			createModal.hide();
			const confirmModal = new bootstrap.Modal("#confirmModal");
			confirmModal.show();
		},
		async handleConfirm() {
			this.message = "";

			// pre-validation
			try {
				const date = new Date(this.roleDeadline);
				const monthNames = [
					"January",
					"February",
					"March",
					"April",
					"May",
					"June",
					"July",
					"August",
					"September",
					"October",
					"November",
					"December",
				];
				const year = date.getFullYear();
				const month = String(date.getMonth() + 1).padStart(2, "0");
				const day = String(date.getDate()).padStart(2, "0");

				const apiURL = `http://localhost:5000/api/createRoleListing`;
				const response = await fetch(apiURL, {
					mode: "cors",
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify({
						name: this.roleName,
						desc: this.roleDescription,
						deadline: `${year}-${month}-${day}`,
					}),
				});
				let data = await response.json();
				if (response.status == 200) {
					this.success = true;
					this.message = data["Status"];
					setTimeout(() => {
						this.success = false;
						location.reload();
					}, globalVars.svgTimeout);
				} else {
					this.error = true;
					this.message = data["error"];
					console.log(this.message);
					setTimeout(() => {
						this.error = false;
					}, globalVars.svgTimeout);
				}
			} catch (error) {
				console.error(error);
			}
		},
	},
};
</script>
