//  Copyright (c) 2021 Intel Corporation
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#ifndef DEEP_ENGINE_EXECUTOR_INCLUDE_OPERATORS_CONCAT_HPP_
#define DEEP_ENGINE_EXECUTOR_INCLUDE_OPERATORS_CONCAT_HPP_
#include <vector>
#include <unordered_map>
#include "oneapi/dnnl/dnnl.hpp"
#include "../operator.hpp"

namespace executor {
using dnnl::memory;
using dnnl::engine;
using dnnl::prop_kind;
using dnnl::algorithm;

/**
 * @brief A Concat operator.
 *
 */

class ConcatOperator : public Operator {
 public:
  explicit ConcatOperator(const OperatorConfig& conf);
  virtual ~ConcatOperator() {}

  void Reshape(const vector<Tensor*>& input, const vector<Tensor*>& output) override;
  void Forward(const vector<Tensor*>& input, const vector<Tensor*>& output) override;

 private:
  int64_t axis_;
  vector<int64_t> dst_shape_;
  bool keep_dims_;
  dnnl::engine eng_ = engine(engine::kind::cpu, 0);
  dnnl::concat concat_p_;
  std::vector<memory> src_m_;
  memory dst_m_;
  unordered_map<int, memory> memory_args_;
};
}  // namespace executor
#endif  // DEEP_ENGINE_EXECUTOR_INCLUDE_OPERATORS_CONCAT_HPP_
