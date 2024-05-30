<template>
    <v-container>
        <div ref="content" v-html="htmlContent"></div>
    </v-container>
</template>


<script>
import apiClient from '@/axios';

export default {
    name: 'NewsContent',
    data() {
    return {
        htmlContent: '',
        error: null,
        };
    },
    created() {
        this.fetchHtmlContent();
    },
    watch: {
        htmlContent() {
            this.$nextTick(() => {
                this.executeScripts();
            });
        }
    },
    beforeRouteUpdate(to, from, next) {
        this.fetchHtmlContent();
        next();
    },
    methods: {
        async fetchHtmlContent() {
            const id = this.$route.query.id;
            try {
                
                const response = await apiClient.get(`/api/news/${id}`);
                this.htmlContent = response.data.content;
            } catch (error) {
                this.error = 'Error fetching HTML content: ' + error.message;
            }
        },
        executeScripts() {
            const contentElement = this.$refs.content;
            const scripts = contentElement.querySelectorAll('script');
            
            scripts.forEach(script => {
                const newScript = document.createElement('script');
                if (script.src) {
                newScript.src = script.src;
                newScript.onload = () => {
                    // console.log(`${script.src} loaded.`);
                };
                newScript.onerror = () => {
                    // console.error(`Failed to load ${script.src}`);
                };
                } else {
                    newScript.textContent = script.textContent;
                }
                document.body.appendChild(newScript).parentNode.removeChild(newScript);
            });
            }
    },
};
</script>

<style>
.photo_center{
    margin: auto;
    display: block;
    width: 100%;
}
</style>