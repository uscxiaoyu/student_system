var clearAlarm = function() {
    var mask_tags = document.getElementsByClassName("display_info")
    for (let mt of mask_tags) {
        mt.style.display = "none";
    }
}

var clearValue = function(input_tg) {
    input_tg.value = ""
};

var formSubmit = function() {
    document.getElementById("myForm").submit()
}

var submitDATA = function() {
    let student_id = document.getElementById("_id").value
    console.log(student_id)
    if (student_id) {
        axios.post("/checkDocx", { s_id: student_id })
            .then(function(res) {
                document.getElementsByClassName("main")[0].style.display = "block";
                var resData = res.data;
                var res_info = document.getElementById("res_info");
                var buttons = document.getElementById("buttons");

                res_info.style.display = "inline";
                res_info.innerHTML = resData;
                if (resData.indexOf("<table") >= 0) { // 如果查询到结果
                    buttons.style.display = "inline";
                }
            })
            .catch(function(err) {
                console.log(err);
            })
    } else {
        console.log("帐号为空!")
    }
}

var updateCertifyState = function(btn, post_url) {
    let sp = btn.parentNode;
    var td = sp.parentNode;
    var p_td = td.previousElementSibling;
    let _id = parseInt(sp.id);
    var btn_content = btn.textContent;
    if (btn_content == "通过") {
        var state = "已认证";
    } else {
        var state = "返修";
    }
    axios({
        method: "post",
        url: post_url,
        data: {
            _id: _id,
            state: state
        }
    }).then(function(res) {
        if (res.data == "更新成功") {
            if (btn_content == "通过") {
                td.parentNode.remove()
            } else {
                p_td.innerHTML = "<span style='background-color: yellow'>反修中</span>"
            }
        } else {
            window.alert("更新失败")
        }
    }).catch(function(res) {
        window.alert(res)
    })
}

var printMe = function() {
    var oldBody = document.body.innerHTML;
    document.body.innerHTML = "<h2>上海对外经贸大学学生第二课堂经历证明</h2>" + document.getElementById('res_info').innerHTML;
    window.print();
    document.body.innerHTML = oldBody // 恢复
}