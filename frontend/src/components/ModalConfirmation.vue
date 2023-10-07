<template>
	<div
		class="modal fade"
		id="confirmModal"
		tabindex="-1"
		aria-labelledby="confirmModalLabel"
		aria-hidden="true">
		<div class="modal-dialog modal-sm h-[calc(100vh-56px)] flex items-center">
			<div class="modal-content">
				<div class="modal-header border-0 p-4">
					<div class="text-h2">Confirmation</div>
					<button
						type="button"
						class="btn-close"
						data-bs-dismiss="modal"
						aria-label="Close"></button>
				</div>
				<div class="modal-body p-4">
					<div class="text-center">
						<ExclamationTriangleIcon class="h-20 w-20 text-warning" />
						<div class="text-h4">Are you sure?</div>
						<div class="">This action cannot be undone.</div>
					</div>
				</div>
				<div class="modal-footer border-0 flex justify-evenly">
					<button
						type="button"
						class="btn btn-secondary text-btn"
						data-bs-dismiss="modal">
						Cancel
					</button>
					<button
						type="button"
						class="btn btn-primary text-btn"
						data-bs-dismiss="modal"
						@click="handleConfirm">
						Confirm
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { ExclamationTriangleIcon } from "@heroicons/vue/24/outline";
export default {
	components: { ExclamationTriangleIcon },
	methods: {
		handleConfirm() {
			this.$emit("confirmed");
		},
	},
};
</script>
