<template>
    <div class="container mx-auto max-w-4xl h-screen w-full mt-12">
        <div class="pt-8">
            <div class="bg-modal p-6 rounded-lg mb-8">
                <div class="flex justify-between items-center">
                    <div class="text-h1">{{ name }}</div>
                    <div class="">Ends: {{ deadline }}</div>
                </div>
                <div class="py-4">Lorem ipsum description</div>
                <div class="flex justify-end gap-4">
                    <button v-if="user.accessRights == 0" class="btn btn-primary text-btn"
                        @click="handleClick">Edit</button>
                    <button class="btn btn-primary text-btn" @click="handleClick">Apply</button>
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
    props: ['name', 'desc', 'description'],
    data() {
        return {
            user: this.$store.state.user,
        };
    },
    created() {

    },
    mounted() {
        console.log(this.name)
    },
    methods: {

    }
}
</script>