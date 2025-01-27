import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: './', // Используйте относительный путь для поддержки в WebView
  build: {
    outDir: 'dist', // Убедитесь, что выводится в папку dist
    assetsDir: 'assets', // Указывает директорию для хранения статических файлов
    rollupOptions: {
      output: {
        assetFileNames: 'assets/[name].[hash][extname]',
        chunkFileNames: 'assets/[name].[hash].js',
        entryFileNames: 'assets/[name].[hash].js',
      },
    },
  },
  server: {
    port: 5173, // Убедитесь, что это совпадает с портом в вашем `docker-compose.yml`
    open: true, // Автоматически открывает браузер при запуске dev-сервера
    headers: {
	'Cache-Control': 'no-cache, no-store, must-revalidate',
    },
 },
});
