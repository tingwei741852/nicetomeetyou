import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home.vue'; 
import NewsContent from '@/components/NewsContent.vue';

Vue.use(Router);
const title = "NBA新聞爬蟲"
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: { title: `${title} | 焦點新聞` }
    },
    {
        path: '/content',
        name: 'NewsContent',
        component: NewsContent,
        meta: { title: `${title} | 新聞詳情` }
    },
  // 在这里添加更多路由
];

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

router.beforeEach((to, from, next) => {
    window.document.title = to.meta.title
    next()
  })

export default router;