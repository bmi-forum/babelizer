// 
// File:          cxx_Component_Impl.cxx
// Symbol:        cxx.Component-v0.0
// Symbol Type:   class
// Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
// Description:   Server-side implementation for cxx.Component
// 
// WARNING: Automatically generated; only changes within splicers preserved
// 
// 
#include "cxx_Component_Impl.hxx"

// 
// Includes for all method dependencies.
// 
#ifndef included_sidl_BaseInterface_hxx
#include "sidl_BaseInterface.hxx"
#endif
#ifndef included_sidl_ClassInfo_hxx
#include "sidl_ClassInfo.hxx"
#endif
#ifndef included_sidl_NotImplementedException_hxx
#include "sidl_NotImplementedException.hxx"
#endif
  // DO-NOT-DELETE splicer.begin(cxx.Component._includes)

  // Insert-UserCode-Here {cxx.Component._includes:prolog} (additional includes or code)

  // Bocca generated code. bocca.protected.begin(cxx.Component._includes)

#define _BOCCA_CTOR_MESSAGES 0
  // If -D_BOCCA_STDERR is given to the compiler, diagnostics print to stderr.
  // In production use, probably want not to use -D_BOCCA_STDERR.
#ifdef _BOCCA_STDERR

#include <iostream>

#ifdef _BOCCA_CTOR_PRINT
#undef _BOCCA_CTOR_MESSAGES
#define _BOCCA_CTOR_MESSAGES 1
#endif // _BOCCA_CTOR_PRINT 
#else  // _BOCCA_STDERR


#endif // _BOCCA_STDERR



  // If -D_BOCCA_BOOST is given to the compiler, exceptions and diagnostics 
  // will include function names for boost-understood compilers.
  // If boost is not available (and therefore ccaffeine is not in use), 
  // -D_BOCCA_BOOST can be omitted and function names will not be included in 
  // messages.
#ifndef _BOCCA_BOOST
#define BOOST_CURRENT_FUNCTION ""
#else
#include <boost/current_function.hpp>
#endif

  // This is intended to simplify exception throwing as SIDL_THROW does for C.
#define BOCCA_THROW_CXX(EX_CLS, MSG) \
{ \
    EX_CLS ex = EX_CLS::_create(); \
    ex.setNote( MSG ); \
    ex.add(__FILE__, __LINE__, BOOST_CURRENT_FUNCTION); \
    throw ex; \
}

  // This simplifies exception extending and rethrowing in c++, like 
  // SIDL_CHECK in C. EX_OBJ must be the caught exception and is extended with 
  // msg and file/line/func added. Continuing the throw is up to the user.
#define BOCCA_EXTEND_THROW_CXX(EX_OBJ, MSG, LINEOFFSET) \
{ \
  std::string msg = std::string(MSG) + std::string(BOOST_CURRENT_FUNCTION); \
  EX_OBJ.add(__FILE__,__LINE__ + LINEOFFSET, msg); \
}


  // Bocca generated code. bocca.protected.end(cxx.Component._includes)

  // Insert-UserCode-Here {cxx.Component._includes:epilog} (additional includes or code)

  // DO-NOT-DELETE splicer.end(cxx.Component._includes)

// special constructor, used for data wrapping(required).  Do not put code here unless you really know what you're doing!
cxx::Component_impl::Component_impl() : StubBase(reinterpret_cast< void*>(
  ::cxx::Component::_wrapObj(reinterpret_cast< void*>(this))),false) , _wrapped(
  true){ 
  // DO-NOT-DELETE splicer.begin(cxx.Component._ctor2)
  // Insert-Code-Here {cxx.Component._ctor2} (ctor2)
  // DO-NOT-DELETE splicer.end(cxx.Component._ctor2)
}

// user defined constructor
void cxx::Component_impl::_ctor() {
  // DO-NOT-DELETE splicer.begin(cxx.Component._ctor)
    
  // Insert-UserCode-Here {cxx.Component._ctor:prolog} (constructor method) 

  // bocca-default-code. User may edit or delete.begin(cxx.Component._ctor)
   #if _BOCCA_CTOR_MESSAGES

     std::cerr << "CTOR cxx.Component: " << BOOST_CURRENT_FUNCTION 
               << " constructing " << this << std::endl;

   #endif // _BOCCA_CTOR_MESSAGES
  // bocca-default-code. User may edit or delete.end(cxx.Component._ctor)

  // Insert-UserCode-Here {cxx.Component._ctor:epilog} (constructor method)

  // DO-NOT-DELETE splicer.end(cxx.Component._ctor)
}

// user defined destructor
void cxx::Component_impl::_dtor() {
  // DO-NOT-DELETE splicer.begin(cxx.Component._dtor)
  // Insert-UserCode-Here {cxx.Component._dtor} (destructor method) 
    
  // bocca-default-code. User may edit or delete.begin(cxx.Component._dtor) 
   #if _BOCCA_CTOR_MESSAGES

     std::cerr << "DTOR cxx.Component: " << BOOST_CURRENT_FUNCTION 
               << " destructing " << this << std::endl;

   #endif // _BOCCA_CTOR_MESSAGES 
  // bocca-default-code. User may edit or delete.end(cxx.Component._dtor) 

  // DO-NOT-DELETE splicer.end(cxx.Component._dtor)
}

// static class initializer
void cxx::Component_impl::_load() {
  // DO-NOT-DELETE splicer.begin(cxx.Component._load)
  // Insert-Code-Here {cxx.Component._load} (class initialization)
  // DO-NOT-DELETE splicer.end(cxx.Component._load)
}

// user defined static methods: (none)

// user defined non-static methods:
/**
 *  This function should never be called, but helps babel generate better code. 
 */
void
cxx::Component_impl::boccaForceUsePortInclude_impl () 

{
  // DO-NOT-DELETE splicer.begin(cxx.Component.boccaForceUsePortInclude)
  // DO-NOT-EDIT-BOCCA
  // Bocca generated code. bocca.protected.begin(cxx.Component.boccaForceUsePortInclude)

  // Bocca generated code. bocca.protected.end(cxx.Component.boccaForceUsePortInclude)
  // DO-NOT-DELETE splicer.end(cxx.Component.boccaForceUsePortInclude)
}

/**
 * Method:  initialize[]
 */
bool
cxx::Component_impl::initialize_impl (
  /* in */const ::std::string& config_file ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.initialize)
  CALL_BMI_VOID(Initialize, config_file.c_str());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.initialize)
}

/**
 * Method:  update[]
 */
bool
cxx::Component_impl::update_impl () 

{
  // DO-NOT-DELETE splicer.begin(cxx.Component.update)
  CALL_BMI_VOID(Update);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.update)
}

/**
 * Method:  update_until[]
 */
bool
cxx::Component_impl::update_until_impl (
  /* in */double time_interval ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.update_until)
  CALL_BMI_VOID(UpdateUntil, time_interval);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.update_until)
}

/**
 * Method:  finalize[]
 */
bool
cxx::Component_impl::finalize_impl () 

{
  // DO-NOT-DELETE splicer.begin(cxx.Component.finalize)
  CALL_BMI_VOID(Finalize);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.finalize)
}

/**
 * Method:  get_start_time[]
 */
int32_t
cxx::Component_impl::get_start_time_impl (
  /* out */double& time ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_start_time)
  CALL_BMI(time, GetStartTime);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_start_time)
}

/**
 * Method:  get_current_time[]
 */
int32_t
cxx::Component_impl::get_current_time_impl (
  /* out */double& time ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_current_time)
  CALL_BMI(time, GetCurrentTime);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_current_time)
}

/**
 * Method:  get_end_time[]
 */
int32_t
cxx::Component_impl::get_end_time_impl (
  /* out */double& time ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_end_time)
  CALL_BMI(time, GetEndTime);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_end_time)
}

/**
 * Method:  get_time_step[]
 */
int32_t
cxx::Component_impl::get_time_step_impl (
  /* out */double& time ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_time_step)
  CALL_BMI(time, GetTimeStep);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_time_step)
}

/**
 * Method:  get_time_units[]
 */
int32_t
cxx::Component_impl::get_time_units_impl (
  /* out */::std::string& units ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_time_units)
  char c_string[2048];
  CALL_BMI_VOID(GetTimeUnits, c_string);
  units = c_string;
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_time_units)
}

/**
 * Method:  get_component_name[]
 */
int32_t
cxx::Component_impl::get_component_name_impl (
  /* out */::std::string& name ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_component_name)
  char c_string[2048];
  CALL_BMI_VOID(GetComponentName, c_string);
  name = c_string;
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_component_name)
}

/**
 * Method:  get_input_item_count[]
 */
int32_t
cxx::Component_impl::get_input_item_count_impl (
  /* out */int32_t& count ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_input_item_count)
  int number_of_names = 0;
  CALL_BMI(number_of_names, GetInputVarNameCount);
  return number_of_names;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_input_item_count)
}

/**
 * Method:  get_output_item_count[]
 */
int32_t
cxx::Component_impl::get_output_item_count_impl (
  /* out */int32_t& count ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_output_item_count)
  int number_of_names = 0;
  CALL_BMI(number_of_names , GetOutputVarNameCount);
  return number_of_names;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_output_item_count)
}

/**
 * Method:  get_input_var_names[]
 */
int32_t
cxx::Component_impl::get_input_var_names_impl (
  /* out array<string> */::sidl::array< ::std::string>& names ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_input_var_names)
  int i;
  int number_of_names = 0;
  char **item_names = NULL;

  CALL_BMI(number_of_names , GetInputVarNameCount);

  item_names = (char**)malloc(sizeof(char*) * number_of_names);
  item_names[0] = (char*)calloc(number_of_names * 2048, sizeof(char));
  for (i = 1; i < number_of_names; i ++) {
    item_names[i] = item_names[i - 1] + 2048;
  }

  CALL_BMI_VOID(GetInputVarNames, item_names);

  names = sidl::array< ::std::string>::create1d(number_of_names);
  for (int i = 0; i < number_of_names; i ++) {
    names.set(i, ::std::string(item_names[i]));
  }
  free(item_names[0]);
  free(item_names);

  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_input_var_names)
}

/**
 * Method:  get_output_var_names[]
 */
int32_t
cxx::Component_impl::get_output_var_names_impl (
  /* out array<string> */::sidl::array< ::std::string>& names ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_output_var_names)
  int i;
  int number_of_names = 0;
  char **item_names = NULL;

  CALL_BMI(number_of_names , GetOutputVarNameCount);

  item_names = (char**)malloc(sizeof(char*) * number_of_names);
  item_names[0] = (char*)calloc(number_of_names * 2048, sizeof(char));
  for (i = 1; i < number_of_names; i ++) {
    item_names[i] = item_names[i - 1] + 2048;
  }

  CALL_BMI_VOID(GetOutputVarNames, item_names);

  names = sidl::array< ::std::string>::create1d(number_of_names);
  for (int i = 0; i < number_of_names; i ++) {
    names.set(i, ::std::string(item_names[i]));
  }
  free(item_names[0]);
  free(item_names);

  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_output_var_names)
}

/**
 * Method:  get_var_type[]
 */
int32_t
cxx::Component_impl::get_var_type_impl (
  /* in */const ::std::string& name,
  /* out */::std::string& type ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_var_type)
  char c_string[2048];
  CALL_BMI_VOID(GetVarType, name.c_str(), c_string);
  type = c_string;
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_var_type)
}

/**
 * Method:  get_var_units[]
 */
int32_t
cxx::Component_impl::get_var_units_impl (
  /* in */const ::std::string& name,
  /* out */::std::string& units ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_var_units)
  char c_string[2048];
  CALL_BMI_VOID(GetVarUnits, name.c_str(), c_string);
  units = c_string;
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_var_units)
}

/**
 * Method:  get_var_nbytes[]
 */
int32_t
cxx::Component_impl::get_var_nbytes_impl (
  /* in */const ::std::string& name,
  /* out */int32_t& nbytes ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_var_nbytes)
  CALL_BMI(nbytes, GetVarNbytes, name.c_str());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_var_nbytes)
}

/**
 * Method:  get_var_itemsize[]
 */
int32_t
cxx::Component_impl::get_var_itemsize_impl (
  /* in */const ::std::string& name,
  /* out */int32_t& size ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_var_itemsize)
  CALL_BMI(size, GetVarItemsize, name.c_str());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_var_itemsize)
}

/**
 * Method:  get_var_grid[]
 */
int32_t
cxx::Component_impl::get_var_grid_impl (
  /* in */const ::std::string& name,
  /* out */int32_t& grid ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_var_grid)
  CALL_BMI(grid, GetVarGrid, name.c_str());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_var_grid)
}

/**
 * Method:  get_grid_type[]
 */
int32_t
cxx::Component_impl::get_grid_type_impl (
  /* in */int32_t grid,
  /* out */::std::string& type ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_type)
  char c_string[2048];
  CALL_BMI_VOID(GetGridType, grid, c_string);
  type = c_string;
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_type)
}

/**
 * Method:  get_grid_rank[]
 */
int32_t
cxx::Component_impl::get_grid_rank_impl (
  /* in */int32_t grid,
  /* out */int32_t& rank ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_rank)
  CALL_BMI(rank, GetGridRank, grid);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_rank)
}

/**
 * Method:  get_grid_size[]
 */
int32_t
cxx::Component_impl::get_grid_size_impl (
  /* in */int32_t grid,
  /* out */int32_t& size ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_size)
  CALL_BMI(size, GetGridSize, grid);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_size)
}

/**
 * Method:  get_grid_shape[]
 */
int32_t
cxx::Component_impl::get_grid_shape_impl (
  /* in */int32_t grid,
  /* in array<int> */::sidl::array<int32_t>& shape ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_shape)
  CALL_BMI_VOID(GetGridShape, grid, shape.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_shape)
}

/**
 * Method:  get_grid_spacing[]
 */
int32_t
cxx::Component_impl::get_grid_spacing_impl (
  /* in */int32_t grid,
  /* in array<double> */::sidl::array<double>& spacing ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_spacing)
  CALL_BMI_VOID(GetGridSpacing, grid, spacing.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_spacing)
}

/**
 * Method:  get_grid_origin[]
 */
int32_t
cxx::Component_impl::get_grid_origin_impl (
  /* in */int32_t grid,
  /* in array<double> */::sidl::array<double>& origin ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_origin)
  CALL_BMI_VOID(GetGridOrigin, grid, origin.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_origin)
}

/**
 * Method:  get_grid_x[]
 */
int32_t
cxx::Component_impl::get_grid_x_impl (
  /* in */int32_t grid,
  /* in array<double> */::sidl::array<double>& x ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_x)
  CALL_BMI_VOID(GetGridX, grid, x.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_x)
}

/**
 * Method:  get_grid_y[]
 */
int32_t
cxx::Component_impl::get_grid_y_impl (
  /* in */int32_t grid,
  /* in array<double> */::sidl::array<double>& y ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_y)
  CALL_BMI_VOID(GetGridY, grid, y.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_y)
}

/**
 * Method:  get_grid_z[]
 */
int32_t
cxx::Component_impl::get_grid_z_impl (
  /* in */int32_t grid,
  /* in array<double> */::sidl::array<double>& z ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_z)
  CALL_BMI_VOID(GetGridZ, grid, z.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_z)
}

/**
 * Method:  get_grid_vertex_count[]
 */
int32_t
cxx::Component_impl::get_grid_vertex_count_impl (
  /* in */int32_t grid,
  /* out */int32_t& n_vertices ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_vertex_count)
  CALL_BMI(n_vertices, GetGridVertexCount, grid);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_vertex_count)
}

/**
 * Method:  get_grid_face_count[]
 */
int32_t
cxx::Component_impl::get_grid_face_count_impl (
  /* in */int32_t grid,
  /* out */int32_t& n_faces ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_face_count)
  CALL_BMI(n_faces, GetGridFaceCount, grid);
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_face_count)
}

/**
 * Method:  get_grid_connectivity[]
 */
int32_t
cxx::Component_impl::get_grid_connectivity_impl (
  /* in */int32_t grid,
  /* in array<int> */::sidl::array<int32_t>& connectivity ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_connectivity)
  CALL_BMI_VOID(GetGridConnectivity, grid, connectivity.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_connectivity)
}

/**
 * Method:  get_grid_offset[]
 */
int32_t
cxx::Component_impl::get_grid_offset_impl (
  /* in */int32_t grid,
  /* in array<int> */::sidl::array<int32_t>& offset ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_grid_offset)
  CALL_BMI_VOID(GetGridOffset, grid, offset.first());
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_grid_offset)
}

/**
 * Method:  get_value[]
 */
int32_t
cxx::Component_impl::get_value_impl (
  /* in */const ::std::string& name,
  /* in array<> */::sidl::basearray& dest ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_value)
  struct sidl__array * array = dest._get_baseior();
  CALL_BMI_VOID(GetValue, name.c_str(),
      sidl_char__array_first((struct sidl_char__array*)(array)));
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_value)
}

/**
 * Method:  get_value_ptr[]
 */
int32_t
cxx::Component_impl::get_value_ptr_impl (
  /* in */const ::std::string& name,
  /* out array<> */::sidl::basearray& values ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_value_ptr)
  void * ptr;
  int size;
  int grid;

  CALL_BMI(grid, GetVarGrid, name.c_str());
  CALL_BMI(size, GetGridSize, grid);
  CALL_BMI(ptr, GetValuePtr, name.c_str());

  if (ptr) {
    const int n_dims = 1;
    const int lower[1] = {0};
    const int upper[1] = {size - 1};
    const int stride[1] = {1};
    sidl::array<char> cvals;
    cvals.borrow((char*)ptr, n_dims, lower, upper, stride);
    values = cvals;
  }

  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.get_value_ptr)
}

/**
 * Method:  get_value_at_indices[]
 */
int32_t
cxx::Component_impl::get_value_at_indices_impl (
  /* in */const ::std::string& name,
  /* in array<> */::sidl::basearray& dest,
  /* in array<int> */::sidl::array<int32_t>& inds ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.get_value_at_indices)
  // Insert-Code-Here {cxx.Component.get_value_at_indices} (get_value_at_indices method)
  // 
  // This method has not been implemented
  // 
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(cxx.Component.get_value_at_indices)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "get_value_at_indices");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(cxx.Component.get_value_at_indices)
  // DO-NOT-DELETE splicer.end(cxx.Component.get_value_at_indices)
}

/**
 * Method:  set_value[]
 */
int32_t
cxx::Component_impl::set_value_impl (
  /* in */const ::std::string& name,
  /* in array<> */::sidl::basearray& values ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.set_value)
  struct sidl__array * array = values._get_baseior();
  CALL_BMI_VOID(SetValue, name.c_str(),
      sidl_char__array_first((struct sidl_char__array*)(array)));
  return 0;
  // DO-NOT-DELETE splicer.end(cxx.Component.set_value)
}

/**
 * Method:  set_value_at_indices[]
 */
int32_t
cxx::Component_impl::set_value_at_indices_impl (
  /* in */const ::std::string& name,
  /* in array<int> */::sidl::array<int32_t>& inds,
  /* in array<> */::sidl::basearray& src ) 
{
  // DO-NOT-DELETE splicer.begin(cxx.Component.set_value_at_indices)
  // Insert-Code-Here {cxx.Component.set_value_at_indices} (set_value_at_indices method)
  // 
  // This method has not been implemented
  // 
  // DO-DELETE-WHEN-IMPLEMENTING exception.begin(cxx.Component.set_value_at_indices)
  ::sidl::NotImplementedException ex = ::sidl::NotImplementedException::_create();
  ex.setNote("This method has not been implemented");
  ex.add(__FILE__, __LINE__, "set_value_at_indices");
  throw ex;
  // DO-DELETE-WHEN-IMPLEMENTING exception.end(cxx.Component.set_value_at_indices)
  // DO-NOT-DELETE splicer.end(cxx.Component.set_value_at_indices)
}


// DO-NOT-DELETE splicer.begin(cxx.Component._misc)
// Insert-Code-Here {cxx.Component._misc} (miscellaneous code)
// DO-NOT-DELETE splicer.end(cxx.Component._misc)

