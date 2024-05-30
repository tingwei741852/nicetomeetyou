<template>
    <v-container class="my-3">
        <!-- <h1>{{message}}</h1> -->
        <h1>焦點新聞</h1>
        <v-divider class="my-3"></v-divider>
         <v-row>
            <v-col cols="6" v-for="(article, index) in news_list" :key="index" class="mt-3">
            <v-row class="hover-background"  @click="redirectToContent(article.id)">
                <v-col cols="5">
                <img :src="article.img_href" alt="" style="width:100%">
                </v-col>
                <v-col cols="7">
                <div class="d-block">
                    <h3>{{article.title}}</h3>
                    <p class="my-1 grey--text text--darken-1">{{article.published_at}}</p>
                </div>
                </v-col>
            </v-row>
            </v-col>
        </v-row>
        <v-snackbar
            v-model="news_update"
            color="success"
            right
            top
            >
            有新的焦點新聞!

            <template v-slot:action="{ attrs }">
                <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="news_update = false"
                >
                Close
                </v-btn>
            </template>
            </v-snackbar>
    </v-container>
</template>


<script>
import apiClient from '@/axios';

export default {
    name: 'Home',
    data() {
        return {
            news_list:[],
            news_update: false,
            message: 'Waiting for news updates...'
        };
    },
    created() {
        this.getNewsList();
        this.$socket.addEventListener('message', this.handleMessage)
    }, 
    methods: {
        async getNewsList() {
            try {
            const response = await apiClient.get('/api/get_focus_news');
            this.news_list = response.data.data;
            } catch (error) {
                console.log(error.message)
            }
        },
        redirectToContent(id) {
            this.$router.push('/content?id=' + id);
        },
        handleMessage(event) {
            const data = JSON.parse(event.data)
            this.message = `${data.status} (${data.created_count} new articles)`
            console.log(data.created_count)
            if (data.created_count > 0) {
                this.getNewsList()
                // console.log("yes")
                this.news_update = true
            }
        }
    },
};
</script>

<style scoped>
.hover-background {
    transition: background-color 0.3s;
    cursor: pointer;
}
.hover-background:hover {
    background-color: #eee; /* 替换为你想要的悬停背景颜色 */
}
</style>