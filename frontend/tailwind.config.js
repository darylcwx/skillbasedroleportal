/** @type {import('tailwindcss').Config} */
export default {
	//prefix: "tw-",
	corePlugins: { preflight: false },
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	theme: {
		extend: {
			colors: {
				navbar: "#181818",
			},
			fontSize: {
				xs: ".75rem", // Extra small font size
				sm: ".875rem", // Small font size
				base: "1rem", // Base font size
				lg: "1.125rem", // Large font size
				xl: "1.25rem", // Extra large font size
				"2xl": "1.5rem", // 2x large font size
				"3xl": "1.875rem", // 3x large font size
				"4xl": "2.25rem", // 4x large font size
				"5xl": "3rem", // 5x large font size
				"6xl": "4rem", // 6x large font size
			},
			fontWeight: {
				thin: "100", // Thin font weight
				extralight: "200", // Extra-light font weight
				light: "300", // Light font weight
				normal: "400", // Normal font weight
				medium: "500", // Medium font weight
				semibold: "600", // Semi-bold font weight
				bold: "700", // Bold font weight
				extrabold: "800", // Extra-bold font weight
				black: "900", // Black font weight
			},
			spacing: {
				76: "19rem",
			},
			height: {
				104: "26rem",
				112: "28rem",
				120: "30rem",
				128: "32rem",
			},
		},
	},
	important: true,
	plugins: [],
};
