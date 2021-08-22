<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted() {  
     // 创建cnzz统计js
    const script = document.createElement('script')  
    const CNZZ_ID = 1280107285
    script.src = `https://s4.cnzz.com/z_stat.php?id=${CNZZ_ID}&web_id=${CNZZ_ID}`  
    script.language = 'JavaScript'  
    document.body.appendChild(script)  
  },  
  watch: {  
    '$route': {
      handler(to, from) {
        setTimeout(() => { //避免首次获取不到window._czc
          if (window._czc) {  
            let location = window.location; 
            let contentUrl = location.pathname + location.hash;  
            let refererUrl = '/';  
            // 用于发送某个URL的PV统计请求，
            window._czc.push(['_trackPageview', contentUrl, refererUrl])  
          }
        }, 300) 
      },
      immediate: true  // 首次进入页面即执行
    }  
  }
}
</script>
