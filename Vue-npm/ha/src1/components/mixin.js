const a = {
    methods: {
        alert() {
            alert(this.name);
        }
    },
    data: function () {
        return {
            // name: 'hello',
            // age: 100,
            sex: 'man'
        }
    },
}
export default a