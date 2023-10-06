<template>
    <div class="bg-[#DBDEE6] rounded-xl mt-4 p-6">
        <!-- Admin -->
        <div class="flex flex-wrap">
            <div class="w-full md:w-1/2">
                <span class="text-h3">Application ID: </span>
                <span class="">{{ application["Application ID"] }}</span>
            </div>
            <div class="w-full md:w-1/2">
                <span class="text-h3">Applicant's Match: </span>
                <span class="">{{ application["Percentage Match"] }}%</span>
            </div>
        </div>
        <div class="flex flex-wrap justify-between">
            <div class="w-full md:w-1/2">
                <span class="text-h3">Staff Name: </span>
                <span class="">{{ application["Staff Name"] }}</span>
            </div>
            <div class="w-full md:w-1/2">
                <span class="text-h3">Staff Department: </span>
                <span class="">{{ application["Staff Dept"] }}</span>

            </div>
        </div>

        <!-- Skills Details -->
        <div class="flex flex-col">
            <div class="flex justify-between items-center mt-6">
                <div class="text-h3">Matched Skills:</div>
            </div>
            <div class="flex flex-wrap">
                <div v-if="this.application['Staff Matched Skills'].length == 0" class="mt-3">
                    Applicant has no matched skills.
                </div>
                <span v-for='skillsMatched in application["Staff Matched Skills"]'
                    class="badge custom-pill bg-success mt-3 mr-3">{{
                        skillsMatched }}
                </span>
            </div>
            <div class="text-h3 mt-6">Other Skills:</div>
        </div>
        <div class="flex flex-wrap">
            <div v-if="this.application['Staff Mismatched Skills'].length == 0" class="mt-3">
                Applicant has no other skills.
            </div>
            <span v-for='skillsMismatched in application["Staff Mismatched Skills"]'
                class="badge custom-pill bg-secondary mt-3 mr-3">{{
                    skillsMismatched }}
            </span>
        </div>
    </div>
</template>
<script>
export default {
    props: ['application'],
    data() {
        return {
            user: this.$store.state.user,
            role: this.$store.state.role,

        };
    },
}

</script>