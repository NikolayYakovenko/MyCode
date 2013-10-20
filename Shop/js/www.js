jQuery(function() 
{
	jQuery(".gallery").jCarouselLite
	(
		{
			visible: 4,
			circular: true,
			scroll: 1,
			speed: 500,
			mouseWheel: true,
			btnNext: ".next",
			btnPrev: ".prev"
		}
	);
});