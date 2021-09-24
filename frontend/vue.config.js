module.exports = {

  lintOnSave: false

}
// module.exports = {
//   devServer: {
//   proxy: { // proxyTable 설정
//     '/accounts': { // api 로 시작하는 소스 는 traget으로 잡아준다. > 사용할때 url 이 api 가 있어야 한다.
//         target: 'https://localhost:8000/', // www.xxx.com
//         changeOrigin: true,
//         // pathRewrite: {
//         //   '^/accounts': ''
//       // }
//         },
//     '/paint_game' : {
//       target: 'https://localhost:8000/',
//       changeOrigin: true,
//       pathRewrite: {
//         '^/paint_game': ''
//     }
//     }
// }
// }
// }
