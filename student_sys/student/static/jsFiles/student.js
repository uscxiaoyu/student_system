var formReset = function() {
    document.querySelector('#add1, #add2').reset()
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
                b.setAttribute("class", "layui-btn-primary layui-btn-sm");
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
    let r_id = parseInt(btn.id) // 记录对应的id有后缀_S或_O
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
            content: `<form id="add2" method="post" class="layui-form">
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