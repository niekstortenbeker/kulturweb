$(document).ready(function(){$('#info').tooltip({trigger:'click hover focus'})});$(document).ready(function(){$('#category-selected').tooltip({trigger:'hover focus'})});let $toggleButtons=$('.toggle-content');let $toggleButtonsDescription=$('.toggle-content-description');let $fullTextWrappers=$('.fulltext');let fullTextWrapper;let toggleButtonText;$fullTextWrappers.attr('hidden',true);$toggleButtons.removeAttr('hidden');$toggleButtonsDescription.removeAttr('hidden');function showMorePattern(beforeText){return function(){$(this).on('click',function(){fullTextWrapper=$(this).parent().find('.fulltext');toggleButtonText=$(this).find('.text');if(!fullTextWrapper.attr('hidden')){toggleButtonText.text(beforeText);fullTextWrapper.attr('hidden',true);$(this).attr('aria-expanded',false)}else{toggleButtonText.text('weniger anzeigen');fullTextWrapper.removeAttr('hidden');$(this).attr('aria-expanded',true)}})}};$toggleButtons.each(showMorePattern('mehr anzeigen'));$toggleButtonsDescription.each(showMorePattern('Beschreibung'));