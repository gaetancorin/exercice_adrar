const btLog = document.getElementById('logBt');
const btReg = document.getElementById('regBt');
const formReg = document.getElementById('reg');
const formLog = document.getElementById('log');

btReg.addEventListener('click', function(){
    btReg.style.display = 'none';
    formReg.style.display = 'block';
    btLog.style.display = 'block';
    formLog.style.display = 'none';
});

btLog.addEventListener('click', function(){
    btLog.style.display = 'none';
    formLog.style.display = 'block';
    btReg.style.display = 'block';
    formReg.style.display = 'none';
});