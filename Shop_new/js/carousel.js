jQuery(function() 
{
	jQuery(".gallery-top").jCarouselLite
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

	jQuery(".gallery-bottom").jCarouselLite
	(
		{
			visible: 4,
			circular: true,
			scroll: 1,
			speed: 500,
			mouseWheel: true,
			btnNext: ".next1",
			btnPrev: ".prev1"
		}
	);
});