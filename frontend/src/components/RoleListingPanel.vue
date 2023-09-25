<template>
    <div class="py-4">
        <div class="p-6 bg-modal rounded-xl text-dark shadow-lg shadow-gray-900">
            <div class="flex justify-between items-center">
                <div class="text-h1">{{ name }}</div>
                <div class="">Ends: <b>{{ deadline }}</b></div>
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
            name: this.role.Role_Name,
            // desc: this.role.description,
            deadline: this.role.Deadline,
        };
    },
    created() {

    },
    mounted() {
        // console.log(this.user);
        // 
    },
    methods: {
        handleClick() {
            // props not being pushed
            this.$router.push({ name: "Role", params: { name: this.name }, props: { description: this.desc, deadline: this.deadline } })
        }
    }
}
</script>