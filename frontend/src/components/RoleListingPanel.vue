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
import { resolveTransitionHooks } from 'vue';

export default {
    props: ['role'],
    data() {
        return {
            user: this.$store.state.user,
            name: this.role.Role_Name,
            desc: this.role.Description,
            deadline: this.role.Deadline,
        };
    },
    created() {

    },
    mounted() {
        // console.log(this.user);
        // console.log(this.role)

    },
    methods: {
        handleClick() {
            // props not being pushed
            this.$store.commit("setRole", {
                    rolename: this.name,
                    description: this.desc,
                    deadline: this.deadline
                });

            this.$router.push({ name: "Role", params: { name: this.name }})
        }
    }
}
</script>