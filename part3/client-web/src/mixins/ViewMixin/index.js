export default {
   methods: {
      getRowClass (i) {
        if (i%2 === 0) {
          return 'pair'
        }
      
        return 'odd';
      }
   }
}
