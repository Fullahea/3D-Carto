Produce_DCM1=f"""阅读示例与生成规则，并仿照示例解析用户输入的语句，生成XML文件。示例如下：
示例1：
Input：Generate a style symbol named 112, with the pipe section of square drainage pipes less than 1m long colored green, and the pipe lines colored blue.
Output：
<?xml version='1.0' encoding='utf-8'?>
<StyleCatalog>
    <FeatureTypeStyle>
        <name>112</name>
        <featureTypeName> drainage pipe</featureTypeName>
        <Rule>
            <name>drainage pipe square transect 1</name>
            <Attribute>square</Attribute>
            <Filter>
                <PropertyBoundary>
                    <LowerBoundary>0.0</LowerBoundary>
                    <UpperBoundary>1.0</UpperBoundary>
                </PropertyBoundary>
            </Filter>
            <SolidSymbolizer>
                <AreaComponent>
                    <Fill>
                        <SvgParameter>
                            <R>0</R>
                            <G>128</G>
                            <B>128</B>
                        </SvgParameter>
                        <Opacity>0.5</Opacity> <!-- 默认透明度 -->
                    </Fill>
                </AreaComponent>
                <LineComponent>
                    <Stroke>
                        <SvgParameter>
                            <R>0</R>
                            <G>0</G>
                            <B>255</B>
                        </SvgParameter>
                    </Stroke>
                </LineComponent>
            </SolidSymbolizer>
        </Rule>
    </FeatureTypeStyle>
</StyleCatalog>
示例2：
Input：Generate a drafting style named 113, with the pipe section of circular rainwater pipes 1~12m long colored yellow with an opacity of 0.7, and the pipe lines colored cyan.
Output：      
<StyleCatalog>
    <FeatureTypeStyle>
        <name>113</name>
        <featureTypeName>rainwater pipe</featureTypeName>
        <Rule>
            <name>rainwater pipe circular transect 1</name>
            <Attribute>circular</Attribute>
            <Filter>
                <PropertyBoundary>
                    <LowerBoundary>1.0</LowerBoundary>
                    <UpperBoundary>12.0</UpperBoundary>
                </PropertyBoundary>
            </Filter>
            <SolidSymbolizer>
                <AreaComponent>
                    <Fill>
                        <SvgParameter>
                            <R>255</R>
                            <G>255</G>
                            <B>0</B>
                        </SvgParameter>
                        <Opacity>0.7</Opacity>
                    </Fill>
                </AreaComponent>
                <LineComponent>
                    <Stroke>
                        <SvgParameter>
                            <R>0</R>
                            <G>128</G>
                            <B>128</B>
                        </SvgParameter>
                    </Stroke>
                </LineComponent>
            </SolidSymbolizer>
        </Rule>
    </FeatureTypeStyle>
</StyleCatalog>
#XML Generation Rules#:
Under the <FeatureTypeStyle> tag, there should be a <name> tag used to describe the style symbol name of the pipe.
The <featureTypeName> tag is used to describe different types of pipes.
The <FeatureTypeStyle> tag can contain multiple <Rule> tags, each defining rules for different categories.
A <Rule> tag includes a <Filter> tag, which contains filtering attributes for the pipe network relevant to the style symbol.
The filtering logic under the <Filter> tag can be set through <Width> or <Length> tags to specify values and ranges, with at least one type specified.
After establishing the filtering logic in the <Rule> tag, the corresponding pipe style must be defined through a <SolidSymbolizer> tag.
Use <PointComponent> for point instantiation of models, with attributes specified within the <Instance> tag.
<LineComponent> and <AreaComponent> are used to implement styling operations for pipeline color and pipe cross-sectional color.
The <LineComponent> tag can also be used for area instantiation.
<ExternalRef> loads all externally referenced models, requiring the addition of the name attribute for the referenced model.
The types that need to be discerned in the <Instance> tag include point-to-point (p2p), line-to-point (l2p), and line-to-line (l2l) instantiation, which need to be identified.
"""
Produce_DCM2="""接下来请根据用户输入语句正确生成XML内容。用户输入语句为："""
Evaluate_DCM="""根据给定的生成规则和评价指标，对生成任务的XML进行评价。需要生成评价报告。
#XML Generation Rules#:
{
Under the <FeatureTypeStyle> tag, there should be a <name> tag used to describe the style symbol name of the pipe.
The <featureTypeName> tag is used to describe different types of pipes.
The <FeatureTypeStyle> tag can contain multiple <Rule> tags, each defining rules for different categories.
A <Rule> tag includes a <Filter> tag, which contains filtering attributes for the pipe network relevant to the style symbol.
The filtering logic under the <Filter> tag can be set through <Width> or <Length> tags to specify values and ranges, with at least one type specified.
After establishing the filtering logic in the <Rule> tag, the corresponding pipe style must be defined through a <SolidSymbolizer> tag.
Use <PointComponent> for point instantiation of models, with attributes specified within the <Instance> tag.
<LineComponent> and <AreaComponent> are used to implement styling operations for pipeline color and pipe cross-sectional color.
The <LineComponent> tag can also be used for area instantiation.
<ExternalRef> loads all externally referenced models, requiring the addition of the name attribute for the referenced model.
The types that need to be discerned in the <Instance> tag include point-to-point (p2p), line-to-point (l2p), and line-to-line (l2l) instantiation, which need to be identified.
}
评价指标：
{
完整性分数（占比10%）：基于必要元素和属性的存在性。
正确性分数（占比10%）：基于元素和属性的结构正确性（如标签嵌套、闭合）。
格式一致性分数（占比20%）：所有数据点的格式正确率。
内容准确度分数（占比40%）：基于内容与预期或参考数据的匹配程度。
差异性分数（占比20%）：识别和计算非一致内容的比例。
}        
"""
Control_Process="""如果在评价的综合得分符合要求，则输出正确的XML，否则重新迭代。"""
