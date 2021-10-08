module.exports = {
  lintOnSave: false,
  // devServer: {
  //   // 프록시 설정
  //   proxy: {
  //     // 프록시 요청을 보낼 api의 시작 부분
  //     '/paint_game': {
  //       // 프록시 요청을 보낼 서버의 주소
  //       target: 'http://j5b307.p.ssafy.io:8000'
  //       // target: 'http://localhost:8000'
  //     },
  //     '/accounts': {
  //       // 프록시 요청을 보낼 서버의 주소
  //       target: 'http://j5b307.p.ssafy.io:8000'
  //       // target: 'http://localhost:8000'

  //     }
  //   }
  // }
  chainWebpack: config => {
    config
      .plugin('html')
      .tap(args => {
        args[0].title = 'Pingo'
        return args
      })
}
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
