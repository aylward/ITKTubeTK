/*=========================================================================
 *
 *  Copyright Insight Software Consortium
 *
 *  Licensed under the Apache License, Version 2.0 ( the "License" );
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *         https://www.apache.org/licenses/LICENSE-2.0.txt
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
*=========================================================================*/
#ifndef __tubeEnhanceTubesUsingDiscriminantAnalysis_hxx
#define __tubeEnhanceTubesUsingDiscriminantAnalysis_hxx



namespace tube
{
template< class TImage, class TLabelMap >
EnhanceTubesUsingDiscriminantAnalysis< TImage, TLabelMap >
::EnhanceTubesUsingDiscriminantAnalysis( void )
{
  m_Filter = FilterType::New();
}

template< class TImage, class TLabelMap >
void
EnhanceTubesUsingDiscriminantAnalysis< TImage, TLabelMap >
::PrintSelf( std::ostream & os, itk::Indent indent ) const
{
  Superclass::PrintSelf( os, indent );

  os << indent << m_Filter << std::endl;
}

} // end namespace tube


#endif
