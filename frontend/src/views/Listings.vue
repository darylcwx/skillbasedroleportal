<template>
    <div class="container mx-auto max-w-4xl h-screen w-full">
        <div class="mt-12">
            <div class="">hi</div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: this.$store.state.user,
            // id, fname lname, dept, email, accessRights
        };
    },
    created() {

    },
    mounted() {
        console.log(this.user);
    },
    methods: {
    }
}
</script>