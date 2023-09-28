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
        <div class="pt-8">
            <div v-if="user.dept == 'HR'" class="custom-modal p-6 rounded-lg shadow-lg shadow-gray-700">
                <div class="text-h1">Applicants</div>
                add applicant component here to show applicant details and their individual role skill match
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['name'],
    data() {
        return {
            user: this.$store.state.user,
            role: this.$store.state.role,
            roleSkillMatch: {},
        };
    },

    created() {

    },

    mounted() {
        this.fetchRoleSkillMatch();
    },

    methods: {
        async fetchRoleSkillMatch() {
            try {
                if (this.user.dept != 'HR') {
                    const apiURL = `http://localhost:5000/api/roleskillmatch?sid=${encodeURIComponent(this.user.id)}&rolename=${encodeURIComponent(this.name)}`;
                    const response = await fetch(apiURL, { mode: "cors" });
                    let roleSkillMatchObject = await response.json();
                    roleSkillMatchObject['Percentage Match'] = parseInt(roleSkillMatchObject['Percentage Match'])
                    this.roleSkillMatch = roleSkillMatchObject
                };

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