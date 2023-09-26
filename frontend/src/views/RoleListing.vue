<template>
    <div class="container mx-auto h-screen max-w-3xl">
        <div class="pt-8">
            <div class="bg-modal p-6 rounded-lg mb-8">
                <div class="flex justify-between items-center">
                    <div class="text-h1">{{ name }}</div>
                    <div class="">Ends: {{ role.deadline }}</div>
                </div>
                <div class="py-4">{{ role.description }}</div>

                <div class="container-fluid">
                    <div class="d-flex justify-end gap-2">
                        <button v-if="user.dept == 'HR'" class="btn btn-primary text-btn" @click="handleEdit">
                            Edit
                        </button>
                        <button class="btn btn-primary text-btn" @click="handleClick">
                            Apply
                        </button>
                    </div>
                </div>



            </div>

            <!-- <div v-if="user.dept == 'HR'" class="bg-modal p-6 rounded-lg">
                <div class="text-h1">Applicants</div>
                add applicant component here to show applicant details and their individual role skill match
            </div> -->

            <div class="bg-modal p-6 rounded-lg">
                <div class="text-h1">Skills Required</div>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col">
                            <span v-for='s in roleskillmatch["Staff Matched Skills"]' class="badge rounded-pill bg-success">Skills matched</span>
                            <span v-for='s in roleskillmatch["Staff Missing Skills"]' class="badge rounded-pill bg-secondary">skills mismatched</span>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <span class="badge rounded-pill" style="color:#274268 ;">percentage match: {{roleskillmatch['Percentage Match']}} %</span>
                        </div>
                    </div>
                </div>
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
        console.log(this.name)
        console.log(this.role)

        this.fetchRoleSkillMatch();
    },

    methods: {
        async fetchRoleSkillMatch() {
            try {
                if (this.user.dept != 'HR'){
                    const apiURL = `http://localhost:5000/api/roleskillmatch?sid=${encodeURIComponent(this.user.id)}&rolename=${encodeURIComponent(this.name)}`;
                    const response = await fetch(apiURL, {mode: "cors"});
                    this.roleskillmatch = await response.json();
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