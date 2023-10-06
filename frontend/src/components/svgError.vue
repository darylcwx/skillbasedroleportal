<template>
	<div
		class="fixed inset-0 flex items-center justify-center w-screen h-screen z-[1040]">
		<div class="absolute bg-overlay opacity-70 w-screen h-screen"></div>
		<div
			class="absolute flex flex-col w-screen h-screen items-center justify-center">
			<div class="icon icon--order-success svg">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="154px"
					height="154px">
					<g
						fill="none"
						stroke="#F44812"
						stroke-width="2">
						<circle
							cx="77"
							cy="77"
							r="72"
							style="
								stroke-dasharray: 480px, 480px;
								stroke-dashoffset: 960px;
							"></circle>
						<circle
							id="colored"
							fill="#F44812"
							cx="77"
							cy="77"
							r="72"
							style="
								stroke-dasharray: 480px, 480px;
								stroke-dashoffset: 960px;
							"></circle>
						<polyline
							class="st0"
							stroke="#fff"
							stroke-width="10"
							points="43.5,77.8  112.2,77.8 "
							style="
								stroke-dasharray: 100px, 100px;
								stroke-dashoffset: 200px;
							" />
					</g>
				</svg>
			</div>
			<div class="text-h2 text-white mt-4">Error!</div>
			<div class="text-white mt-1">{{ this.message }}</div>
		</div>
	</div>
</template>
<script>
export default {
	props: ["message"],
};
</script>
<style>
.w4rAnimated_checkmark svg {
	width: 100px;
	display: block;
	margin: 40px auto 0;
}
.w4rAnimated_checkmark .path {
	stroke-dasharray: 1000;
	stroke-dashoffset: 0;
}
.w4rAnimated_checkmark .path.circle {
	-webkit-animation: dash 0.9s ease-in-out;
	animation: dash 0.9s ease-in-out;
}
.w4rAnimated_checkmark .path.line {
	stroke-dashoffset: 1000;
	-webkit-animation: dash 0.9s 0.35s ease-in-out forwards;
	animation: dash 0.9s 0.35s ease-in-out forwards;
}
.w4rAnimated_checkmark .path.check {
	stroke-dashoffset: -100;
	-webkit-animation: dash-check 0.9s 0.35s ease-in-out forwards;
	animation: dash-check 0.9s 0.35s ease-in-out forwards;
}

@-webkit-keyframes dash {
	0% {
		stroke-dashoffset: 1000;
	}
	100% {
		stroke-dashoffset: 0;
	}
}
@keyframes dash {
	0% {
		stroke-dashoffset: 1000;
	}
	100% {
		stroke-dashoffset: 0;
	}
}
@-webkit-keyframes dash-check {
	0% {
		stroke-dashoffset: -100;
	}
	100% {
		stroke-dashoffset: 900;
	}
}
@keyframes dash-check {
	0% {
		stroke-dashoffset: -100;
	}
	100% {
		stroke-dashoffset: 900;
	}
}

.animation-ctn {
	text-align: center;
	margin-top: 5em;
}

@-webkit-keyframes checkmark {
	0% {
		stroke-dashoffset: 100px;
	}

	100% {
		stroke-dashoffset: 200px;
	}
}

@-ms-keyframes checkmark {
	0% {
		stroke-dashoffset: 100px;
	}

	100% {
		stroke-dashoffset: 200px;
	}
}

@keyframes checkmark {
	0% {
		stroke-dashoffset: 100px;
	}

	100% {
		stroke-dashoffset: 0px;
	}
}

@-webkit-keyframes checkmark-circle {
	0% {
		stroke-dashoffset: 480px;
	}

	100% {
		stroke-dashoffset: 960px;
	}
}

@-ms-keyframes checkmark-circle {
	0% {
		stroke-dashoffset: 240px;
	}

	100% {
		stroke-dashoffset: 480px;
	}
}

@keyframes checkmark-circle {
	0% {
		stroke-dashoffset: 480px;
	}

	100% {
		stroke-dashoffset: 960px;
	}
}

@keyframes colored-circle {
	0% {
		opacity: 0;
	}

	100% {
		opacity: 100;
	}
}

/* other styles */
/* .svg svg {
      display: none
  }
   */
.inlinesvg .svg svg {
	display: inline;
}

/* .svg img {
      display: none
  } */

.icon--order-success svg polyline {
	-webkit-animation: checkmark 0.25s ease-in-out 0.7s backwards;
	animation: checkmark 0.25s ease-in-out 0.7s backwards;
}

.icon--order-success svg circle {
	-webkit-animation: checkmark-circle 0.6s ease-in-out backwards;
	animation: checkmark-circle 0.6s ease-in-out backwards;
}
.icon--order-success svg circle#colored {
	-webkit-animation: colored-circle 0.6s ease-in-out 0.7s backwards;
	animation: colored-circle 0.6s ease-in-out 0.7s backwards;
}
</style>
