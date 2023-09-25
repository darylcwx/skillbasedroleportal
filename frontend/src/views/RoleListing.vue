<template>
    <div class="container mx-auto h-screen">
        <div class="pt-8">
            <div class="bg-modal p-6 rounded-lg mb-8">
                <div class="flex justify-between items-center">
                    <div class="text-h1">{{ name }}</div>
                    <div class="">Ends: {{ deadline }}</div>
                </div>
                <div class="py-4">{{ description }}</div>

                <div class="container-fluid">
                    <div class="row">
                        <div class="col">
                            <span class="badge rounded-pill bg-success">Skills matched</span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <span class="badge rounded-pill bg-secondary">skills mismatched</span>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <span class="badge rounded-pill" style="color:#274268 ;">percentage match</span>
                        </div>
                    </div>

                    <div class="d-flex justify-end gap-2">
                        <button v-if="user.accessRights == 0" class="btn btn-primary text-btn" @click="handleEdit">
                            Edit
                        </button>
                        <button class="btn btn-primary text-btn" @click="handleClick">
                            Apply
                        </button>
                    </div>
                </div>



            </div>
            <div v-if="user.accessRights == 0" class="bg-modal p-6 rounded-lg">
                <div class="text-h1">Applicants</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['name', 'description', 'deadline'],
    data() {
        return {
            user: this.$store.state.user,
        };
    },
    created() {

    },
    mounted() {
        console.log(this.name)
        // either push props into page or call getRole?id= ... again
        // returning undefined, can only passed through params. name is ok, desc and deadline is not
        console.log(this.description)
        console.log(this.deadline)
    },
    methods: {
        handleEdit() {

        },
        handleApply() {

        }
    }
}
</script>