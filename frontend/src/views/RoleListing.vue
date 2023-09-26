<template>
    <div class="container mx-auto h-screen max-w-2xl">
        <div class="pt-8">
            <div class="custom-modal p-6 rounded-lg mb-8">
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

            <!-- Skills Required -->
            <div class="custom-modal p-6 rounded-lg">
                <div class="flex items-center justify-between">
                    <div class="text-h1 mr-4">Skills Required</div>
                    <div name="percentage" class="">Percentage match: {{ roleskillmatch['Percentage Match'] }} %</div>
                </div>
                <div name="matched" class="mt-4 flex-col">
                    <span v-for='skillsMatched in roleskillmatch["Staff Matched Skills"]'
                        class="badge custom-pill bg-success mt-3 mr-3">{{
                            skillsMatched }}
                    </span>
                    <span v-for='skillsMismatched in roleskillmatch["Staff Missing Skills"]'
                        class="badge custom-pill bg-secondary mt-3 mr-3">{{
                            skillsMismatched }}
                    </span>
                </div>
            </div>

            <!-- Applicants -->
            <div v-if="user.dept == 'HR'" class="custom-modal p-6 rounded-lg">
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
            roleskillmatch: {},
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
                    // percentage to 0 d.p.
                    roleSkillMatchObject['Percentage Match'] = parseInt(roleSkillMatchObject['Percentage Match'])
                    this.roleskillmatch = roleSkillMatchObject
                };

            } catch (error) {
                console.error("There was a problem with the fetch operation:", error);
            }
        },

        handleEdit() {

        },
        handleApply() {

        }

    }
}
</script>