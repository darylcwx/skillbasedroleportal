<template>
    <div class="container mx-auto max-w-2xl min-h-[calc(100vh-56px)] mt-14">
        <!-- Role details -->
        <div class="pt-8">
            <div class="custom-modal p-6 rounded-lg shadow-lg shadow-gray-700">
                <div class="flex justify-between items-center">
                    <div class="text-h1 mr-4">{{ name }}</div>
                    <div class="">Ends: {{ role.deadline }}</div>
                </div>
                <div class="mt-4">{{ role.description }}</div>
                <div class="flex justify-end gap-2 mt-4">
                    <button v-if="user.accessRights == 0" class="btn btn-primary text-btn" @click="handleEdit">
                        Edit
                    </button>
                    <button class="btn btn-primary text-btn" @click="handleClick">
                        Apply
                    </button>
                </div>
            </div>
        </div>

        <!-- Skills Required -->
        <div class="pt-8">
            <div class="custom-modal p-6 rounded-lg shadow-lg shadow-gray-700">
                <div class="flex items-center justify-between">
                    <div class="text-h1 mr-4">Skills Required</div>
                    <div v-if="Object.keys(roleSkillMatch).length == 0" class="">
                        Percentage match: ... %
                    </div>
                    <div v-else class="">
                        Percentage match: {{ roleSkillMatch['Percentage Match'] }}%
                    </div>
                </div>
                <div name="matched" class="mt-4 flex-col">
                    <div v-if="Object.keys(roleSkillMatch).length == 0" class="placeholder-wave">
                        <span class="placeholder col-3 badge custom-pill-no-shadow bg-secondary text-secondary mt-3 mr-3">
                            placeholder
                        </span>
                        <span class="placeholder col-5 badge custom-pill-no-shadow bg-secondary text-secondary mt-3 mr-3">
                            placeholder
                        </span>
                        <span class="placeholder col-4 badge custom-pill-no-shadow bg-secondary text-secondary mt-3 mr-3">
                            placeholder
                        </span>
                        <span class="placeholder col-2 badge custom-pill-no-shadow bg-secondary text-secondary mt-3 mr-3">
                            placeholder
                        </span>
                        <span class="placeholder col-9 badge custom-pill-no-shadow bg-secondary text-secondary mt-3 mr-3">
                            placeholder
                        </span>
                    </div>
                    <span v-for='skillsMatched in roleSkillMatch["Staff Matched Skills"]'
                        class="badge custom-pill bg-success mt-3 mr-3">{{
                            skillsMatched }}
                    </span>
                    <span v-for='skillsMismatched in roleSkillMatch["Staff Missing Skills"]'
                        class="badge custom-pill bg-secondary mt-3 mr-3">{{
                            skillsMismatched }}
                    </span>
                </div>
            </div>
        </div>

        <!-- Applicants -->
        <div class="pt-8 pb-8">
            <!-- need to change the v-if -->
            <div v-if="user.dept == 'HR'" class="custom-modal p-6 rounded-lg shadow-lg shadow-gray-700">
                <div class="text-h1">Applicants</div>
                <div v-for="applicant of this.applicants">
                    <Application :application="applicant" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Application from '../components/Application.vue'
export default {
    props: ['name'],
    components: { Application },
    data() {
        return {
            user: this.$store.state.user,
            role: this.$store.state.role,
            roleSkillMatch: {},
            applicants: [],
        };
    },

    created() {

    },

    mounted() {
        this.fetchRoleSkillMatch();
        this.fetchAllApplicants();
    },

    methods: {
        async fetchRoleSkillMatch() {
            try {
                const apiURL = `http://localhost:5000/api/roleskillmatch?sid=${encodeURIComponent(this.user.id)}&rolename=${encodeURIComponent(this.name)}`;
                const response = await fetch(apiURL, { mode: "cors" });
                let roleSkillMatchObject = await response.json();
                roleSkillMatchObject['Percentage Match'] = parseInt(roleSkillMatchObject['Percentage Match'])
                this.roleSkillMatch = roleSkillMatchObject

            } catch (error) {
                console.error(error);
            }
        },

        async fetchAllApplicants() {
            try {
                const apiURL = `http://localhost:5000/api/allroleskillmatch?lid=${encodeURIComponent(this.role.listingID)}`;
                const response = await fetch(apiURL, { mode: "cors" });
                let applicantObject = await response.json();

                for (let i in applicantObject['Applicants']) {
                    applicantObject['Applicants'][i]['Percentage Match'] = parseInt(applicantObject['Applicants'][i]['Percentage Match'])
                }

                this.applicants = applicantObject['Applicants']
                // [ {'Application ID', 'Staff Name', 'Staff Dept',  
                // 'Staff Matched Skills', 'Staff Mismatched Skills', 'Percentage Match'} ]
                console.log(this.applicants)
            } catch (error) {
                console.error(error);
            }
        },

        handleEdit() {

        },
        handleApply() {

        }

    }
}
</script>