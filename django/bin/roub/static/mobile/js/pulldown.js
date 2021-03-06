function pullDownAction () {	//下拉刷新
	window.location.reload();
}

function loaded() {
	var pullDownEl = document.getElementById('pullDown');
	var pullDownOffset = pullDownEl.offsetHeight;
	// var pullDownOffset = 96;

	var myScroll = new iScroll('wrapper', {
		// useTransition: true,
		hScroll: false,
		hScrollbar: false,
		vScrollbar: false,
		topOffset: pullDownOffset,
		onRefresh: function () {
			if (pullDownEl.className.match('loading')) {
				pullDownEl.className = '';
				// pullDownEl.querySelector('.pullDownLabel').innerHTML = '下拉即可刷新';
			}
		},
		onScrollMove: function () {
			if (this.y > 5 && !pullDownEl.className.match('flip')) {
				pullDownEl.className = 'flip';
				// pullDownEl.querySelector('.pullDownLabel').innerHTML = '松开即可刷新';
				this.minScrollY = 0;
			} else if (this.y < 5 && pullDownEl.className.match('flip')) {
				pullDownEl.className = '';
				// pullDownEl.querySelector('.pullDownLabel').innerHTML = '下拉即可刷新';
				this.minScrollY = -pullDownOffset;
			}
		},
		onScrollEnd: function () {
			if (pullDownEl.className.match('flip')) {
				pullDownEl.className = 'loading';
				pullDownEl.querySelector('.pullDownLabel').innerHTML = '努力加载中...';
				pullDownAction();	// Execute custom function (ajax call?)
			}
		}
	});
	// setTimeout(function () { document.getElementById('wrapper').style.left = '0'; }, 300);
}

document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);

document.addEventListener('DOMContentLoaded', loaded, false);