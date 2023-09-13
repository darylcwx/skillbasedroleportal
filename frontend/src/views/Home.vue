<template>
    <div class="container h-screen w-full flex row justify-center items-center">
        <div class="grid grid-cols-2 gap-8">
            <div v-for="item in 4">
                <div class="p-8 bg-accent rounded-xl text-black">
                    <div class="pb-9">Name of Module {{ item }}</div>
                    <div class="">Link here</div>
                </div>
            </div>
            <div v-if="role == 'Human Resources'" class="p-8 bg-accent rounded-xl text-black">HR module </div>
            <div v-if="role == 'Staff'" class="p-8 bg-accent rounded-xl text-black">staff module </div>
            <div v-if="role == 'Manager'" class="p-8 bg-accent rounded-xl text-black">manager module </div>
        </div>

    </div>
</template>
<script>
export default {
    props: ['role'],
    data() {
        return {
        };
    },
    created() {

    },
    mounted() {

    },
    methods() {

    }
}
</script>