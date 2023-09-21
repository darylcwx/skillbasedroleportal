<template>
    <div class="py-4">
        <div class="p-6 bg-modal rounded-xl text-black">
            <div class="flex justify-between items-center">
                <div class="text-h1">{{ name }}</div>
                <div class="">Ends: {{ deadline }}</div>
            </div>
            <div class="py-4">{{ desc }}</div>
            <div class="flex justify-end gap-4">
                <button class="btn btn-primary text-btn" @click="handleClick">See more</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['role'],
    data() {
        return {
            user: this.$store.state.user,
            name: this.role.roleName,
            desc: this.role.roleDesc,
            deadline: this.role.roleDeadline,
        };
    },
    created() {

    },
    mounted() {
        console.log(this.user);
    },
    methods: {
        handleClick() {
            this.$router.push({ name: "Role", params: { name: this.name }, props: { desc: this.desc, deadline: this.deadline } })
        }
    }
}
</script>