$.fn.selectMatch = function(options) {
	// 常量变量
	var SELECT = 'select', SELECTED = 'selected', DISABLED = 'disabled',  ACTIVE = 'active', REVERSE = 'reverse';

	// 默认参数
	var defaults = {
		prefix: 'ui-',    // 一些UI样式类名的前缀
		trigger: ['change']     // 触发原始下拉框的事件，默认只触发change事件
	};
	// 参数合并
	var params = $.extend({}, defaults, options || {});
	
	// 通用前缀
	var PREFIX = params.prefix + SELECT, joiner = params.prefix.replace(/[a-z]/gi, '');
	
	// 根据下拉框获得相关数据的私有方法
	var _get = function(el) {
		var selectedIndex = 0, htmlOptions = '';
		
		// 遍历下拉框的options选项
		el.find('option').each(function(index) {
			var arrCl = [PREFIX + joiner + 'datalist'+ joiner +'li', this.className];
			
			if (this[SELECTED]) {
				selectedIndex = index;
				arrCl.push(SELECTED); 
			}
			if (this[DISABLED]) {
				arrCl.push(DISABLED); 
			}
			
			htmlOptions = htmlOptions + '<li class="'+ arrCl.join(' ') +'" data-index='+ index +'>'+ this.innerHTML +'</li>';
		});
		
		return {
			index: selectedIndex,
			html: htmlOptions
		}
	}

	return $(this).each(function(index, element) {
        var sel = $(this).hide().data(SELECT);
		if (!sel) {
			// 如果没有关联的模拟下拉元素生成
			// 创建新的模拟下拉元素
			sel = $('<div></div>').on('click', 'a', function() {
				if ($(element).prop(DISABLED)) return false;
				// 显示与隐藏
				sel.toggleClass(ACTIVE);
				// 边界判断
				if (sel.hasClass(ACTIVE)) {
					var ul = sel.find('ul'), 
					overflow = ul.offset().top + ul.outerHeight() > Math.max($(document.body).height(), $(window).height());
					sel[overflow? 'addClass': 'removeClass'](REVERSE);

					// 滚动与定位
					var arrData = sel.data('scrollTop'), selected = ul.find('.' + SELECTED);
					// 严格验证
					if (arrData && arrData[1] == selected.attr('data-index') && arrData[2] == selected.text()) {
						ul.scrollTop(arrData[0]);
						// 重置
						sel.removeData('scrollTop');
					}						
				} else {
					sel.removeClass(REVERSE);
				}
			}).on('click', 'li', function(event, istrigger) {
				var indexOption = $(this).attr('data-index'),
					scrollTop = $(this).parent().scrollTop();	
				// 下拉收起
				sel.removeClass(ACTIVE);
				// 存储可能的滚动定位需要的数据
				sel.data('scrollTop', [scrollTop, indexOption, $(this).text()]);
				// 修改下拉选中项
				$(element).find('option').eq(indexOption).get(0)[SELECTED] = true;
				// 更新下拉框
				$(element).selectMatch(params);
				// 回调处理
                $.each(params.trigger, function(i, eventType) {
					$(element).trigger(eventType, [istrigger]);	
				});
			});
			// 存储对象
			$(this).data(SELECT, sel);
			// 载入元素
			$(this).after(sel);
			
			// 点击页面空白要隐藏
			$(document).mouseup(function(event) {
				var target = event.target;
				if (target && sel.hasClass(ACTIVE) && sel.get(0) !== target && sel.get(0).contains(target) == false) {
					sel.removeClass(ACTIVE).removeClass(REVERSE);
				}
			});
		}
		
		// 根据当前下拉元素，重新刷新
		// 0. 获得我们需要的一些数据
		var data = _get($(this)), option = $(this).find('option').eq(data.index);
		// 1. 与select元素匹配的类名, 以及宽度
		sel.attr('class', element.className + ' ' + PREFIX).width($(this).outerWidth());
		// 2. 全新的按钮元素
        var areaNo = option.html().split(' ')[0];
        var button = '<a href="javascript:" class="'+ PREFIX + joiner + 'button">'+
            '<span class="'+ PREFIX + joiner + 'text">' + areaNo + '</span>'+
            '<i class="'+ PREFIX + joiner + 'icon"></i></a>';
		// 3. 全新的列表
		var datalist = '<ul class="'+ PREFIX + joiner + 'datalist">'+ data.html +'</ul>';
		
		// 4. 刷新
		sel.html(button + datalist);
    });
};

$('select').selectMatch();