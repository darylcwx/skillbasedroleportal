<template>
    <div class="bg-[#e7ecff] border border-2 rounded-lg mt-4 p-4">
        <!-- Admin -->
        <table>
            <tr>
                <td>

                </td>
                <td>

                </td>
            </tr>
            <tr>
                <td>

                </td>
                <td>

                </td>
            </tr>
        </table>
        <div class="flex flex-wrap">
            <div class="w-full md:w-1/2">
                <span class="text-h3">Application ID: </span>
                <span class="">{{ application["Application ID"] }}</span>
            </div>
            <div class="w-full md:w-1/2">
                <span class="text-h3">Percentage Match (to role): </span>
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
            <div class="flex justify-between items-center mt-4">
                <div class="text-h3">Matched Skills:</div>
            </div>
            <div class="flex flex-wrap">
                <span v-for='skillsMatched in application["Staff Matched Skills"]'
                    class="badge custom-pill bg-success mt-3 mr-3">{{
                        skillsMatched }}
                </span>
            </div>
            <div class="text-h3 mt-4">Mismatched Skills:</div>
        </div>
        <div class="flex flex-wrap">
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