<template>
    <!-- This container will encapsulate all content-->
    <div class="container mx-auto max-w-4x1 h-screen w-full mt-12">
        <div class="pt-8">
            <div class="custom-modal p-10 rounded-lg mb-8">
                <!-- Create a href at the top left, to go back previous listing page or "X" -->
                <!-- Align items center -->
                <div class="flex justify-between items-center pt-4">
                    <!--Below is hardcoded for now, am trying to familiarize myself with the syntax-->
                    <div class="text-h1">Software Engineer</div>
                    <div class="opacity-75">Created Time</div>
                    <div class="opacity-75">Expiry Date</div>
                </div>
                <!-- This section will be for the specified role description -->
                <div class="py-4">
                    We are seeking a talented and motivated Software Engineer to join our dynamic team. As a Software Engineer, you will play a pivotal role in designing, developing, and maintaining cutting-edge software solutions. You'll collaborate with cross-functional teams to translate business requirements into scalable and efficient software systems. The ideal candidate is passionate about technology, possesses strong problem-solving skills, and has a proven track record of delivering high-quality code. Join us in shaping the future of our products and contributing to our mission of delivering innovative software solutions to our customers
                </div>

                <!-- Return to previous page -->
                <!-- Button to Apply -->
                <div class="flex justify-between items-center pt-4">
                    <a href="#" class="text-blue-500 :underline"> Return to Main Listing</a>
                    <button class="btn btn-primary text-btn">Apply for Role</button>
                </div>

            </div>
        </div>
    </div>
</template>