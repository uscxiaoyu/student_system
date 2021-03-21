var formReset = function() {
    document.querySelector('#add1, #add2, #update1, #update2').reset()
};

var getFormValues = function(form) { // 获取表单中的input值
    var data = new Object();
    var tagElements = form.getElementsByTagName('input');
    for (var i = 0; i < tagElements.length; i++) {
        data[tagElements[i].name] = tagElements[i].value.trim();
    }
    return data;
};

var submitData = function(form_tag, tb_tag, post_url, del_url) {
    let form = document.getElementById(form_tag);
    let post_data = getFormValues(form);
    axios.post(post_url, post_data)
        .then(function(res) {
            window.alert("添加成功!");
            if (post_url.indexOf('Org') >= 0) {
                var r_id = `${res.data.id}` + '_O';
            } else {
                var r_id = `${res.data.id}` + '_S';
            }

            console.log(res);
            if (res.status == 200) {
                tb = document.getElementById(tb_tag);
                trs = tb.getElementsByTagName("tr");
                last_tr = trs[trs.length - 1];
                last_idx = parseInt(last_tr.querySelector("th, td").textContent); // 获取上一个序号
                if (last_idx) {
                    idx = (last_idx + 1).toString();
                } else {
                    idx = "1";
                };
                var new_tr = document.createElement("tr"); // 新的一行
                var idx_td = document.createElement("td");
                idx_td.appendChild(document.createTextNode(idx));
                new_tr.appendChild(idx_td);
                for (let ele in post_data) {
                    td = document.createElement("td");
                    td.appendChild(document.createTextNode(post_data[ele]));
                    new_tr.appendChild(td);
                };
                td = document.createElement("td");
                td.appendChild(document.createTextNode("未认证"));
                new_tr.appendChild(td);

                td = document.createElement("td");
                b = document.createElement("button");
                b.setAttribute("id", r_id);
                b.setAttribute("onclick", `deleteData(this, '${del_url}')`)
                b.setAttribute("class", "layui-btn layui-btn-danger layui-btn-sm");
                b.appendChild(document.createTextNode("删除"));
                td.appendChild(b);
                new_tr.appendChild(td);

                last_tr.parentNode.appendChild(new_tr);
            } else {
                window.alert("添加失败");
            }
        })
        .catch(function(err) {
            window.alert(err);
        });
};

var deleteData = function(btn, del_url) {
    let tr = btn.parentNode.parentNode; // 记录对应的行
    let r_id = parseInt(btn.parentNode.id) // 记录对应button父节点的id有后缀_S或_O
    axios({
        method: 'get',
        url: del_url + `/${r_id}`
    }).then(function(res) {
        console.log(res.data)
        if (res.status == 200) {
            window.alert('删除成功')
            tr.remove();
        }
    }).catch(function(err) {
        window.alert(err);
    });
};

var open_layer1 = function() {
    layui.use('layer', function() {
        var layer = layui.layer;
        layer.open({
            type: 1,
            title: "<p style='text-align:center;font-size:1.5em; font-weight:bold'>学生组织记录</p>",
            area: ["400px", "450px"],
            content: `<form id="add1" class="layui-form">
                        <div class="layui-input-block">
                            <label class="layui-form-label">开始时间</label>
                            <div class="layui-input-block">
                                <input type="date" lay-verify="required" id="start_time" name="start_time" value="" class="layui-input"/>
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">结束时间</label>
                            <div class="layui-input-block">
                                <input type="date" lay-verify="required" id="end_time" name="end_time" value="" class="layui-input"/>
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">组织名称</label>
                            <div class="layui-input-block">
                                <input type="text" lay-verify="required" id="org_name" name="org_name" value="" class="layui-input">
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">职位</label>
                            <div class="layui-input-block">
                                <input type="text" lay-verify="required" id="position" name="position" value="" class="layui-input">
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">隶属部门</label>
                            <div class="layui-input-block">
                                <input type="text" lay-verify="required" id=department_name name="department_name" value="" class="layui-input">
                            </div>
                        </div>
                    </form>
                    <div class="layui-input-block">
                        <div class="layui-form-item">
                            <button class="layui-btn-primary layui-btn-sm" onclick="submitData('add1', 'studentOrgTB', '/insertStudentOrganization', '/deleteStudentOrganization')">提交</button>
                            <button class="layui-btn-primary layui-btn-sm layui-btn-primary" onclick="formReset()">清空</button>
                        </div>
                    </div>`
        });
    })
};

var open_layer2 = function() {
    layui.use('layer', function() {
        var layer = layui.layer;
        layer.open({
            type: 1,
            title: "<p style='text-align:center; font-size:1.5em; font-weight:bold'>奖励记录</p>",
            area: ["400px", "300px"],
            content: `<form id="add2" class="layui-form">
                            <div class="layui-input-block">
                                <label class="layui-form-label">奖励时间</label>
                                <div class="layui-input-block">
                                    <input type="date" lay-verify="required" name="g_time" value="" class="layui-input"/>
                                </div>
                            </div>
                            <div class="layui-input-block">
                                <label class="layui-form-label">奖励名称</label>
                                <div class="layui-input-block">
                                    <input type="text" name="scholar_name" value="" class="layui-input" lay-verify="required">
                                </div>
                            </div>
                            <div class="layui-input-block">
                                <label class="layui-form-label">奖励级别</label>
                                <div class="layui-input-block">
                                    <input type="text" name="level" value="" class="layui-input" lay-verify="required">
                                </div>
                            </div>
                        </form>
                        <div class="layui-form-item">
                            <div class="layui-input-block">
                                <button class="layui-btn-primary layui-btn-sm" onclick="submitData('add2', 'studentScholarTB', '/insertStudentScholar', '/deleteStudentScholar')">提交</button>
                                <button class="layui-btn-primary layui-btn-sm layui-btn-primary" onclick="formReset()">清空</button>
                            </div>
                        </div>`
        });
    })
};


var open_layer3 = function(btn) {
    let _id = parseInt(btn.parentNode.id);
    let tr = btn.parentNode.parentNode
    let tds = tr.querySelectorAll("td")
    var ori_data = {
        _id: _id,
        "start_time": tds[1].textContent.trim(),
        "end_time": tds[2].textContent.trim(),
        "org_name": tds[3].textContent.trim(),
        "position": tds[4].textContent.trim(),
        "department_name": tds[5].textContent.trim()
    };
    var content = `<form id="update1" class="layui-form">
                        <div class="layui-input-block">
                            <label class="layui-form-label">开始时间</label>
                            <div class="layui-input-block">
                                <input type="date" lay-verify="required" id="start_time" name="start_time" value="${ori_data.start_time}" class="layui-input"/>
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">结束时间</label>
                            <div class="layui-input-block">
                                <input type="date" lay-verify="required" id="end_time" name="end_time" value="${ori_data.end_time}" class="layui-input"/>
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">组织名称</label>
                            <div class="layui-input-block">
                                <input type="text" lay-verify="required" id="org_name" name="org_name" value="${ori_data.org_name}" class="layui-input">
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">职位</label>
                            <div class="layui-input-block">
                                <input type="text" lay-verify="required" id="position" name="position" value="${ori_data.position}" class="layui-input">
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">隶属部门</label>
                            <div class="layui-input-block">
                                <input type="text" lay-verify="required" id=department_name name="department_name" value="${ori_data.department_name}" class="layui-input">
                            </div>
                        </div>
                    </form>
                    <div class="layui-input-block">
                        <div class="layui-form-item">
                            <button class="layui-btn-primary layui-btn-sm" onclick="updateStudentOrganization(${ori_data._id})">提交</button>
                        </div>
                    </div>`

    layui.use('layer', function() {
        var layer = layui.layer;
        layer.open({
            type: 1,
            title: "<p style='text-align:center;font-size:1.5em; font-weight:bold'>学生组织记录</p>",
            area: ["400px", "420px"],
            content: content
        });
    })
}

var updateStudentOrganization = function(_id) {
    let inputs = document.querySelectorAll("#update1 input");
    var new_data = {
        "_id": _id,
        "start_time": inputs[0].value.trim(),
        "end_time": inputs[1].value.trim(),
        "org_name": inputs[2].value.trim(),
        "position": inputs[3].value.trim(),
        "department_name": inputs[4].value.trim()
    };
    axios({
        method: "post",
        url: "/updateStudentOrganization",
        data: new_data
    }).then(function(res) {
        if (res.data == "更新成功") {
            window.alert(res.data);
            tr = document.getElementById(`${new_data._id}_O`).parentNode;
            tds = tr.querySelectorAll('td');
            tds[1].textContent = new_data.start_time;
            tds[2].textContent = new_data.end_time;
            tds[3].textContent = new_data.org_name;
            tds[4].textContent = new_data.position;
            tds[5].textContent = new_data.department_name;
            tds[6].textContent = "未认证";
        } else {
            window.alert(res.data);
        }
    }).catch(function(error) {
        window.alert(error)
    });

}


var open_layer4 = function(btn) {
    let _id = parseInt(btn.parentNode.id);
    let tr = btn.parentNode.parentNode
    let tds = tr.querySelectorAll("td")
    var ori_data = {
        _id: _id,
        "g_time": tds[1].textContent.trim(),
        "scholar_name": tds[2].textContent.trim(),
        "level": tds[3].textContent.trim(),
    };
    console.log(ori_data)
    var content = `<form id="update2" class="layui-form">
                        <div class="layui-input-block">
                            <label class="layui-form-label">奖励时间</label>
                            <div class="layui-input-block">
                                <input type="date" lay-verify="required" name="g_time" value="${ori_data.g_time}" class="layui-input"/>
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">奖励名称</label>
                            <div class="layui-input-block">
                                <input type="text" name="scholar_name" value="${ori_data.scholar_name}" class="layui-input" lay-verify="required">
                            </div>
                        </div>
                        <div class="layui-input-block">
                            <label class="layui-form-label">奖励级别</label>
                            <div class="layui-input-block">
                                <input type="text" name="level" value="${ori_data.level}" class="layui-input" lay-verify="required">
                            </div>
                        </div>
                    </form>
                    <div class="layui-form-item">
                        <div class="layui-input-block">
                            <button class="layui-btn-primary layui-btn-sm" onclick="updateStudentScholar(${ori_data._id})">提交</button>
                        </div>
                    </div>`

    layui.use('layer', function() {
        var layer = layui.layer;
        layer.open({
            type: 1,
            title: "<p style='text-align:center;font-size:1.5em; font-weight:bold'>学生奖学金记录</p>",
            area: ["400px", "300px"],
            content: content
        });
    })
}

var updateStudentScholar = function(_id) {
    let inputs = document.querySelectorAll("#update2 input");
    var new_data = {
        "_id": _id,
        "g_time": inputs[0].value.trim(),
        "scholar_name": inputs[1].value.trim(),
        "level": inputs[2].value.trim(),
    };
    axios({
        method: "post",
        url: "/updateStudentScholar",
        data: new_data
    }).then(function(res) {
        if (res.data == "更新成功") {
            window.alert(res.data);
            tr = document.getElementById(`${new_data._id}_S`).parentNode;
            tds = tr.querySelectorAll('td');
            tds[1].textContent = new_data.g_time;
            tds[2].textContent = new_data.scholar_name;
            tds[3].textContent = new_data.level;
            tds[4].textContent = "未认证";
        } else {
            window.alert(res.data);
        }
    }).catch(function(error) {
        window.alert(error)
    });

}