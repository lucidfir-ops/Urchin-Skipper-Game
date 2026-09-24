// itch.io hosts each upload beneath a CDN subdirectory.
export default {
  base: './',
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          phaser: ['phaser'],
          'terrain-data': ['./src/generated/sectors.json'],
        },
      },
    },
  },
};
