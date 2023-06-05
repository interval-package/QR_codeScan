var numberPresent={
    0:{
        "A":"0001101",
        "B":"0100111",
        "C":"1110010"
    },
    1:{
        "A":"0011001",
        "B":"0110011",
        "C":"1100110"
    },
    2:{
        "A":"0010011",
        "B":"0011011",
        "C":"1101100"
    },
    3:{
        "A":"0111101",
        "B":"0100001",
        "C":"1000010"
    },
    4:{
        "A":"0100011",
        "B":"0011101",
        "C":"1011100"
    },
    5:{
        "A":"0110001",
        "B":"0111001",
        "C":"1001110"
    },
    6:{
        "A":"0101111",
        "B":"0000101",
        "C":"1010000"
    },
    7:{
        "A":"0111011",
        "B":"0010001",
        "C":"1000100"
    },
    8:{
        "A":"0110111",
        "B":"0001001",
        "C":"1001000"
    },
    9:{
        "A":"0001011",
        "B":"0010111",
        "C":"1110100"
    }
}

var version=[
    ["A","A","A","A","A","A"],
    ["A","A","B","A","B","B"],
    ["A","A","B","B","A","B"],
    ["A","A","B","B","B","A"],
    ["A","B","A","A","B","B"],
    ["A","B","B","A","A","B"],
    ["A","B","B","B","A","A"],
    ["A","B","A","B","A","B"],
    ["A","B","A","B","B","A"],
    ["A","B","B","A","B","A"]
];


function produceCodeBar () {
    var content = document.getElementById("input_box").value;
    console.log(content.length);
    if(content.length!==12){
        alert("请输入合法条码(12位，不包含校验码)");
    }
    else {
        var num=new Array();
        var even=0;
        var odd=0;
        for(var i=0;i<12;i++){
            num[11-i]=parseInt(content%10);
            content/=10;
            // 记录奇数位偶数位数字之和
            if(i%2==1){
                odd+=num[11-i]; //奇数位
            }
            else
                even+=num[11-i]; //偶数位
        }
        var check=even*3+odd;
        num[12]=10-check%10;
        console.log(num[12]);
        var temp = "<div><div class='bar_long color_1'></div><div class='bar_long color_0'></div><div class='bar_long color_1'></div>";
        for(var i=1;i<=6;i++){
            var ver = num[0];//取前置位
            var choosen=version[ver][i-1];//通过前置位得到对应的前六位AB子集
            var numTemp = parseInt(numberPresent[num[i]][choosen]);
            for(var j=0;j<7;j++){
                if(parseInt(numTemp/Math.pow(10,6-j))===0){
                    temp+="<div class='bar color_0'></div>";
                }
                else{
                    temp+="<div class='bar color_1'></div>"
                }
                numTemp%=Math.pow(10,6-j);
            }
        }
        temp+=
            "<div class='bar_long color_0'></div><div class='bar_long color_1'></div>" +
            "<div class='bar_long color_0'></div><div class='bar_long color_1'></div>" +
            "<div class='bar_long color_0'></div>";
        for(var i=7;i<13;i++){
            var numTemp = parseInt(numberPresent[num[i]].C);
            for(var j=0;j<7;j++){
                if(parseInt(numTemp/Math.pow(10,6-j))===0){
                    temp+="<div class='bar color_0'></div>";
                }
                else{
                    temp+="<div class='bar color_1'></div>"
                }
                numTemp%=Math.pow(10,6-j);
            }
        }
        temp+=
            "<div class='bar_long color_1'></div><div class='bar_long color_0'></div>" +
            "<div class='bar_long color_1'></div><div class='clearfix'></div> ";
        $("#code_bar").html(temp);

        var temp="<div class='numNum start'>"+num[0]+"</div>";
       // temp+=""
        for(var i=1;i<7;i++){
            temp+="<div class='numNum dataPart'>"+num[i]+"</div>";
        }
        temp+="<div class='numNum center'></div>";
        for(var i=7;i<13;i++){
            temp+="<div class='numNum dataPart'>"+num[i]+"</div>";
        }
        temp+="<div class='clearfix'></div>";
        $("#num_position").html(temp);
    }
}
//6921311140312