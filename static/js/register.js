

/*
DOM树加载完成后需要做的事情
包含初始化的行为操作 如 :事件的绑定
 */

$(function(){
	// 为手机号码框绑定失去焦点检测事件
	$("#uphone").blur(isPhone);

	// 为密码框绑定失去焦点检测时间
	$("#upwd").blur(isPassword);

	console.log($('#uemail'));
	// 绑定邮箱检测
	// 为#frm_register 绑定submit 事件
	$('#frm_register').submit(function(){
		return checkEmail()&&isPhone()&&isPassword();
	});
})





function isPhone(){
	/*
		功能 : 检查手机号码是否符合规范
		返回值 : 
			true : 验证通过
			false : 验证未通过
	 */
	uphone = $("#uphone").val(); //获取uphone的值
	$show = $("#uphone-show") // 获取显示的jq对象
	// 向window中增加一个变量,默认值为false
	window.flag = false;
	// 验证手机号为空
	if(uphone == ''){
		$show.html("手机号不能为空");
	}else{
		//正则表达式判断手机格式是否符合要求
		if(/^1[3456789]\d{9}$/.test(uphone) ==false){
			$show.html("请输入正确的手机格式")
			return false;
		}
		// AJAX验证服务器端是否有相同的数据
		$.ajax({
			url:"/uphonec/",
			type :'post',
			data : {
				"uphone":uphone,
				"csrfmiddlewaretoken":$.cookie('csrftoken')
			},
			dataType : "json",
			success : function(data){
				if(data.status == 1){
					$show.html("通过");
					return true;
				}else{
					$show.html('已存在');
					return false;
				}

			}
		})
	}
}


function isPassword(){
	if($("#upwd").val() == ''){
		$("#upwd-show").html("密码不能为空")
		return false
	}else if($("#upwd").val().length < 6){
		$("#upwd-show").html("请输入6位以上的密码")
		return false
	}else{
		$("#upwd-show").html("通过")
		return true;
	}


}

function checkEmail(){
	var uemail = $("#uemail").val();
	var $show = $("#uemail-show");
	if(uemail!== ""){
		$show.html('邮箱不能为空')
		return false;
	}else if(/\d+@\d+\.\d/.test(uemail)){
		$show.html('请输入正确的游戏格式')
		return false;
	}else{
		$show.html('通过');
		return true;
	}
}



