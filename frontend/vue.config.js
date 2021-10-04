module.exports = {
  lintOnSave: false,
  devServer: {
    // 프록시 설정
    proxy: {
      // 프록시 요청을 보낼 api의 시작 부분
      '/paint_game': {
        // 프록시 요청을 보낼 서버의 주소
        target: 'http://localhost:8000'
      },
      '/accounts': {
        // 프록시 요청을 보낼 서버의 주소
        target: 'http://localhost:8000'
      }
    }
  }
}
