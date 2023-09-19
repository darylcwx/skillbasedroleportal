<template>
    <div class="p-8 bg-accent rounded-xl text-black">
        <div class="text-h1">{{ name }}</div>
        <div class="py-4">{{ description }}</div>
        <button class="btn btn-primary" @click="handleClick">Continue</button>
    </div>
</template>

<script>
export default {
    props: ['name', 'description', 'path'],
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
        handleClick() {
            this.$router.push({ name: "Listings" })
        }
    }
}
</script>