function YuewenAuthen(params) {
	
	this.apiUrl = params.apiUrl;
	
	var config =  {
		appId: '10',
        areaId: 1,        
        format: 'jsonp'
	};
	
	this.authInfo = {
		account: '', //账号
        guid: '',
        sessionKey: '', //图片验证码使用-个性化注册
        phonekey: '' //手机验证码使用	
	};
	
	this.ajaxUrl = {
	    checkAccount: this.apiUrl + '/userSdk/checkaccount',
	    getCaptcha: this.apiUrl + '/userSdk/getvalidatecode',
	    getVerificationCode: this.apiUrl + '/userSdk/sendmsgnew',
	    doRegister: this.apiUrl + '/userSdk/doregister',
	    confirmEmail: this.apiUrl + '/userSdk/confirmemail',
	    reSendRegEmail: this.apiUrl + '/userSdk/resendregemail',
	    phoneCodeLogin: this.apiUrl + '/userSdk/phonecodelogin',
	    checkLoginStatus: this.apiUrl + '/login/checkStatus',
	    reSendMsg: this.apiUrl + '/userSdk/resendmsg',
        getFastRegValidateCode: this.apiUrl + '/userSdk/getValidateCodeNew'
	};
	
	if(config) this.config = params;
	
	this.checkAccount = function(account, accountType, callback) {	
		var config = this.config;
		
		var data = { 
			appId: config.appId, 
			format: config.format,
			account: account, 
			accountType: accountType, 
			areaId:config.areaId
		};
		
		this.jsonp(this.ajaxUrl.checkAccount, data, callback);
	};
	
	this.getCaptcha = function(force, callback) {
		var config = this.config;
		
		var data = {
		    appId: config.appId, 
			format: config.format,
			areaId: config.areaId,
			force: force
		}
		
		this.jsonp(this.ajaxUrl.getCaptcha, data, callback);
	};
	
	//兼容验证类型
	this.getCaptchaType = function (force,callback) {
        var config = this.config;

        var data = {
            appId: config.appId,
            format: config.format,
            areaId: config.areaId,
            force: force
        }

        this.jsonp(this.ajaxUrl.getFastRegValidateCode, data, callback);
    }
	
	this.getVerificationCode = function(phone, phoneIsAbroad, type, sessionKey, validateCode, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId:  config.areaId,
			inputUserId: phone,
			type: type,
			sessionKey: sessionKey,
			phoneIsAbroad: phoneIsAbroad == true ? 1 : 0,
			validateCode: validateCode
		}
	    
	    this.jsonp(this.ajaxUrl.getVerificationCode, data, callback);
	};
	
	this.sendPhoneCheckCode = function(phone, phoneIsAbroad, type, sessionKey, validateCode, needRegister, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId:  config.areaId,
			inputUserId: phone,
			type: type,
			sessionKey: sessionKey,
			phoneIsAbroad: phoneIsAbroad == true ? 1 : 0,
			validateCode: validateCode,
			needRegister: needRegister
		}
	    this.jsonp(this.ajaxUrl.getVerificationCode, data, callback);
	};
	
	this.reSendPhoneCheckCode = function(phone, phoneIsAbroad, type, needRegister, sk, st, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId:  config.areaId,
			inputUserId: phone,
			type: type,
			phoneIsAbroad: phoneIsAbroad == true ? 1 : 0,
			needRegister: needRegister,
			sk: sk,
			st: st
		}
	    this.jsonp(this.ajaxUrl.reSendMsg, data, callback);
	};
	
	this.doRegisterByPhone = function (account, phone, phoneIsAbroad, accountType, password, phoneKey, phoneCode, backUrl, callback) {     
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId:config.areaId,
			account: account,
			mobile: phone,
			accountType: accountType,
			password: password,
			phoneKey: phoneKey,
			phoneCode: phoneCode,
			phoneIsAbroad: phoneIsAbroad,
			ticket: config.ticket ? config.ticket : 0,
            returnUrl: config.backUrl ? (config.backUrl) : ''
		}

        if($("#txtcard").length > 0) data.card = $("#txtcard").val();
	    
	    this.jsonp(this.ajaxUrl.doRegister, data, callback);
	};
	
	this.doRegisterByEmail = function(account, email, accountType, password, sessionKey, validateCode, backUrl, ajaxdm, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId: config.areaId,
			account: account,
			email: email,
			accountType: accountType,
			password: password,
            sessionKey: sessionKey,
            validateCode: validateCode,
            backUrl:backUrl,
            ajaxdm:ajaxdm,
            from:config.from
		}
	    
	    this.jsonp(this.ajaxUrl.doRegister, data, callback);
	}
	
	this.confirmEmail = function(emailKey, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId: config.areaId,
			emailKey: emailKey
		}
	    
	    this.jsonp(this.ajaxUrl.confirmEmail, data, callback);
	};
	
	this.reSendRegEmail = function(emailKey, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId: config.areaId,
			emailKey: emailKey
		}
	    
	    this.jsonp(this.ajaxUrl.reSendRegEmail, data, callback);
	};
	
	this.phoneCodeLogin = function(phone, phoneKey, code, callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId: config.areaId,
			inputuserid: phone,
			sessionkey: phoneKey,
			validatecode: code,
			ticket: config.ticket ? config.ticket : 0,
            returnUrl: config.backUrl ? (config.backUrl) : ''
		}
	    
	    this.jsonp(this.ajaxUrl.phoneCodeLogin, data, callback);
	};
	
	this.checkLoginStatus = function(callback) {
		var config = this.config;
	    var data = {
		    appId: config.appId, 
			format: config.format,
			areaId: config.areaId,
			returnurl: config.backUrl
		}
	    
	    this.jsonp(this.ajaxUrl.checkLoginStatus, data, callback);
	};
	
	this.jsonp = function(url, data, success) {		
        $.ajax({
            type: "get",
            url: url,
            data: data,
            dataType: "jsonp",
            jsonp: 'method',
            success: success || function() {},
            timeout: 10000,
            error:function() {
            	//手机登录注册
            	if(typeof(Register) != 'undefined') {
            		try {
            			Register.showLiteTip('内部服务器错误请重试！');
            			$(".red-btn").removeClass('loading');
            			Register.isRegistering = false;
            			Register.isChecking = false;
            			$('#get-code').html(Register.tips.reSendMsg);
            		} catch(e) {
            			
            		}
            	}
            	if(typeof(QRegister) != 'undefined') {
            		try {
            			alert('内部服务器错误请重试！');
            			QRegister.mailCloseLoading();
            			QRegister.closeLoading();
            		} catch(e) {
            			
            		}
            	}
            }
        });
	}
}

function ajaxCallBack(data){

}