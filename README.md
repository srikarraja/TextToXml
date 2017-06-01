## Welcome to TextToXml Pages

You can use the [editor on GitHub](https://github.com/srikarraja/TextToXml/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### TextToXml

TextToXml is a light weight and easy-to-use python application with just 54 lines of code for formatting messed up XML to proper Formatter XML

```markdown
Syntax highlighted code block

# Before converting

<?xml version="1.0"?><Living Animals><Vertebrates><Mammels><intellegent>Humans</intellegent><Non intellegent>Dog</intellegent></Mammels><Non Mammels><Birds>Hen</Birds></Non Mammels></Vertebrates><Invertibrates><Reptiles>Snake</Reptiles><Plants></Plants></Invertibrates></Living Animals>

## After Converting 
<?xml version="1.0"?>
<Living Animals>
	<Vertebrates>
		<Mammels>
			<intellegent>Humans</intellegent>
			<Non intellegent>Dog</intellegent>
		</Mammels>
		<Non Mammels>
			<Birds>Hen</Birds>
		</Non Mammels>
	</Vertebrates>
	<Invertibrates>
		<Reptiles>Snake</Reptiles>
		<Plants></Plants>
	</Invertibrates>
</Living Animals>




**Bold** and _Italic_ and `Code` text

[Link](https://github.com/srikarraja/TextToXml/) and ![Image](TextToXml/Capture.PNG)
```

For more details see [GitHub Flavored Markdown](https://srikarraja.github.io/TextToXml/).


### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
