<template>
    <div class="d-flex flex-row align-items-stretch mt-4">
        <div class="flex-grow-1 mr-3">
            <div class="input-group rounded">
                <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search" aria-describedby="search-addon" />
            </div>
        </div>
        
        <div class="dropdown">
            <button class="btn btn-primary dropdown-toggle"
                    type="button"
                    id="multiSelectDropdown"
                    data-bs-toggle="dropdown"
                    aria-expanded="false">
                <!-- {{ dropdownButtonText }} -->
                Filter
            </button>
            <ul class="dropdown-menu"
                aria-labelledby="multiSelectDropdown">
                <li v-for="(item, index) in items" :key="index">
                <label class="ml-2">
                    <!-- <input type="checkbox" :value="item.value" v-model="item.selected" @change="handleCheckboxChange" /> -->
                    <input type="checkbox" :value="item.value" v-model="item.selected" />
                    {{ item.label }}
                </label>
                </li>
            </ul>
        </div>
    </div>

</template>

<script>
export default {
data() {
    return {
    items: [
        { label: "Java", value: "Java", selected: false },
        { label: "C++", value: "C++", selected: false },
        { label: "Python", value: "Python", selected: false },
    ],
    };
},
computed: {
    dropdownButtonText() {
    const selectedItems = this.items.filter((item) => item.selected).map((item) => item.label);
    return selectedItems.length > 0 ? selectedItems.join(', ') : 'Select Items';
    },
},
methods: {
},
mounted() {
    const dropdownButton = document.getElementById('multiSelectDropdown');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    dropdownMenu.addEventListener('change', this.handleCheckboxChange);
},
};
</script>
